# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../" && pwd)"

# Activate virtual environment
source "$PROJECT_ROOT/wsheet-env/bin/activate"

# Run all pytest-based tests in this directory
echo "Running all tests in tests/metadata_utils with virutalenv..."
pytest "$SCRIPT_DIR"
