from metadata_utils import MetadataUtils

openai_api_key = "..." 

problem_text = """Pierādīt, ka skaitļi 3n+2 un 7n+5 ir savstarpēji pirmskaitļi."""

metadata = MetadataUtils(openai_api_key)

predicted_type = metadata.classify_problem(problem_text, '', 'questionType')

print(f"Predicted questionType: {predicted_type}")
