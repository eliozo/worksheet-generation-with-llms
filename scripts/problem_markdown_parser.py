import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class Problem:
    """Represents a single math problem parsed from a markdown file."""
    title: str
    full_problem: str  # everything after the # heading, before next heading
    grade: int = 0
    meta_dict: Dict[str, List[str]] = field(default_factory=dict)
    problem_text: str = ""      # text above <small> block (no metadata, no solution)
    solution_text: str = ""     # text starting from ## Atrisinājums / ## Solution


class ProblemMarkdownParser:
    """Parses math problem markdown files into Problem objects."""

    HEADING_RE = re.compile(r'^#\s+<lo-sample/>\s+(.*)')
    SMALL_BLOCK_RE = re.compile(r'(<small>)(.*?)(</small>)', re.DOTALL)

    # ------------------------------------------------------------------ #
    #  Core parsing: file -> list of Problem
    # ------------------------------------------------------------------ #

    @classmethod
    def parse_file(cls, filepath: str) -> List[Problem]:
        """Read a markdown file and return a list of Problem objects."""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        return cls.parse_text(text)

    @classmethod
    def parse_text(cls, text: str) -> List[Problem]:
        """Parse raw markdown text into a list of Problem objects."""
        raw_sections = cls.extract_sections(text)
        problems = []
        for title, body in raw_sections:
            p = Problem(title=title.strip(), full_problem=body)
            p.grade = cls.extract_grade(p.title)
            p.meta_dict = cls.extract_metadata(p.full_problem)
            p.problem_text = cls.normalize_text(p.full_problem)
            p.solution_text = cls.extract_solution(p.full_problem)
            problems.append(p)
        return problems

    # ------------------------------------------------------------------ #
    #  Section splitting
    # ------------------------------------------------------------------ #

    @classmethod
    def extract_sections(cls, text: str) -> List[Tuple[str, str]]:
        """Split markdown text into (title, body) pairs by # <lo-sample/> headings."""
        sections: List[Tuple[str, str]] = []
        current_body: Optional[str] = None
        title = "NA"

        for line in text.splitlines(keepends=True):
            m = cls.HEADING_RE.match(line)
            if m:
                new_title = m.group(1)
                if current_body is not None:
                    sections.append((title, current_body))
                title = new_title
                current_body = ''
            elif current_body is not None:
                current_body += line

        if current_body is not None:
            sections.append((title, current_body))
        return sections

    @classmethod
    def extract_sections_from_file(cls, filepath: str) -> List[Tuple[str, str]]:
        """Read a file and return raw (title, body) pairs."""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        return cls.extract_sections(text)

    # ------------------------------------------------------------------ #
    #  Text normalization / extraction helpers
    # ------------------------------------------------------------------ #

    @staticmethod
    def normalize_text(text: str) -> str:
        """Return problem text stripped of the <small>…</small> metadata block and everything after it."""
        meta_start = text.find('<small>')
        if meta_start > 0:
            return text[:meta_start].strip()
        # If no <small> block, strip solution headings too
        for marker in ('## Atrisin', '## Solution'):
            pos = text.find(marker)
            if pos >= 0:
                return text[:pos].strip()
        return text.strip()

    @staticmethod
    def extract_solution(text: str) -> str:
        """Return everything from the first solution heading (## Atrisinājums or ## Solution) onward."""
        for marker in ('## Atrisin', '## Solution'):
            pos = text.find(marker)
            if pos >= 0:
                return text[pos:].strip()
        # Fallback: content after </small>
        f1 = text.find('</small>')
        if f1 >= 0:
            return text[f1 + len('</small>'):].strip()
        return ""

    @staticmethod
    def get_solutions(text: str) -> List[str]:
        """Split the solution portion into individual solution blocks."""
        if not text:
            return []
        header_re = re.compile(r'(?m)^##\s+(Atrisinājums|Solution)(?:-\d+)?\s*$')
        matches = list(header_re.finditer(text))
        if not matches:
            return [text] if text.strip() else []
        sections = []
        for i, m in enumerate(matches):
            start = m.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            sections.append(text[start:end])
        return sections

    # ------------------------------------------------------------------ #
    #  Metadata extraction
    # ------------------------------------------------------------------ #

    @staticmethod
    def extract_metadata(text: str) -> Dict[str, List[str]]:
        """Parse the <small>…</small> block into a metadata dictionary."""
        metadata: Dict[str, List[str]] = {}
        lines = text.split('\n')
        meta_opened = False
        for line in lines:
            if re.fullmatch(r'\s*<small>\s*', line):
                meta_opened = True
            elif re.fullmatch(r'\s*</small>\s*', line):
                meta_opened = False
                break
            elif meta_opened:
                if line.startswith('* ['):
                    continue
                key_val = line.split(":")
                if len(key_val) >= 2:
                    key = key_val[0]
                    if key.startswith('* '):
                        key = key[2:]
                    value_str = ":".join(key_val[1:])
                    values = value_str.split(",")
                    if key in metadata:
                        metadata[key].extend([v.strip() for v in values])
                    else:
                        metadata[key] = [v.strip() for v in values]
        # Merge "_domain" into "domain": "domain" takes precedence; "_domain" is removed.
        if '_domain' in metadata:
            if 'domain' not in metadata or not any(metadata['domain']):
                metadata['domain'] = metadata['_domain']
            del metadata['_domain']
        return metadata

    # ------------------------------------------------------------------ #
    #  Grade extraction from title
    # ------------------------------------------------------------------ #

    @staticmethod
    def extract_grade(title: str) -> int:
        """Extract grade (int) from a problem title like LV.AMO.2023.5.1 (grade = 5)."""
        parts = title.strip().split('.')
        if len(parts) >= 2:
            grade_str = parts[-2]
            m = re.match(r'^(\d+)', grade_str)
            if m:
                return int(m.group(1))
        return 0

    # ------------------------------------------------------------------ #
    #  Problem text extraction (for RDF etc.)
    # ------------------------------------------------------------------ #

    @staticmethod
    def extract_problem_body(section_text: str) -> str:
        """Extract pure problem text (no heading, no <small> block, no solution)."""
        lines = section_text.split('\n')
        result = []
        for line in lines:
            if line.startswith('# '):
                continue
            elif re.fullmatch(r'^\s*<small>\s*', line) or re.fullmatch(r'## .*', line):
                break
            else:
                result.append(line)
        return '\n'.join(result)

    # ------------------------------------------------------------------ #
    #  Image extraction
    # ------------------------------------------------------------------ #

    @staticmethod
    def extract_images(text: str) -> List[Tuple[str, str]]:
        """Return list of (image_src, width) from markdown image references."""
        images = []
        image_regex = re.compile(r"^!\[.*\]\((.*)\)(\{\s*width=(\S*)\s*\})?")
        for line in text.split('\n'):
            line = line.strip()
            match = image_regex.match(line)
            if match:
                image_id = match.group(1)
                width = match.group(3) if match.group(3) else ''
                images.append((image_id, width))
        return images

    # ------------------------------------------------------------------ #
    #  Metadata modification (for add_metadata workflow)
    # ------------------------------------------------------------------ #

    @classmethod
    def add_generated_property(cls, md_text: str, prop_name: str, generated_val) -> str:
        """Insert a generated metadata property into the <small>…</small> block."""
        match = cls.SMALL_BLOCK_RE.search(md_text)
        check_tag = f"_{prop_name}:"

        if not match:
            return md_text

        before_tag = match.group(1)
        middle_block = match.group(2)
        after_tag = match.group(3)

        prop_marker = f'_{prop_name}:'
        if prop_marker in middle_block:
            return md_text

        existing_content = middle_block.strip()

        lines_to_add = []
        if isinstance(generated_val, dict):
            if prop_name == "hasSolutionConcept":
                main_val = generated_val.get('solutionConcepts') or generated_val.get('concepts', [])
                rd_val = generated_val.get('readingDifficulty')
                if isinstance(main_val, list):
                    val_str = ", ".join(main_val)
                else:
                    val_str = str(main_val)
                lines_to_add.append(f"* {check_tag} {val_str}")
                if rd_val:
                    lines_to_add.append(f"* _readingDifficulty: {rd_val}")
            elif prop_name == "hasReasoningMethod":
                methods = generated_val.get('methods', [])
                if isinstance(methods, list):
                    val_str = ", ".join(methods)
                else:
                    val_str = str(methods)
                lines_to_add.append(f"* {check_tag} {val_str}")
                new_method = generated_val.get('newMethod')
                if new_method and isinstance(new_method, dict):
                    new_label = new_method.get('label', '')
                    new_desc = new_method.get('shortDescriptionEn', '')
                    if new_label:
                        lines_to_add.append(f"* _newReasoningMethodLabel: {new_label}")
                    if new_desc:
                        lines_to_add.append(f"* _newReasoningMethodDescription: {new_desc}")
            else:
                val_main = generated_val.get(prop_name, [])
                if isinstance(val_main, list):
                    val_str = ", ".join(val_main)
                else:
                    val_str = str(val_main)
                lines_to_add.append(f"* {check_tag} {val_str}")
                alt_key = f"{prop_name}_alternative"
                alt_val = generated_val.get(alt_key)
                if alt_val:
                    lines_to_add.append(f"* _{alt_key}: {alt_val}")
        else:
            lines_to_add.append(f"* {check_tag} {generated_val}")

        new_str = "\n".join(lines_to_add)
        if existing_content:
            new_content = existing_content + "\n" + new_str
        else:
            new_content = new_str

        updated_block = f"{before_tag}\n\n{new_content}\n\n{after_tag}"
        return md_text[:match.start()] + updated_block + md_text[match.end():]
