"""
Main script for the project.
"""
from logging_utils import setup_logger

log = setup_logger()


def main():
    """Main function to run the script."""
    log.info("🚀 Starting main process...")
    try:
        # Your code logic here
        print("Hello World!")
        log.info("✅ Main process completed.")
    except Exception as e:
        log.exception(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
