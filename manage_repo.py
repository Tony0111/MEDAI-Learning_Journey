import os
import subprocess
import time
import sys

GITIGNORE_CONTENT = """
# Ignore large data files and directories
data/
*.nii.gz
*.gz
*.zip
*.tar.gz
*.npy
*.pt
*.pth
*.h5
*.hdf5
.DS_Store
__pycache__/
*.pyc
venv/
env/
.env
*.env
*.log

# Ignore IDE/editor specific files
.vscode/
.idea/
*.swp
"""

def run_command(command, ignore_errors=False, capture_output=True):
    """Runs a shell command and returns its output."""
    print(f"Executing: {' '.join(command)}")
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True # Use shell=True for simplicity on Windows with paths, or specific shell if needed
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0 and not ignore_errors:
            print(f"Error executing command: {' '.join(command)}")
            print(f"Return code: {process.returncode}")
            print(f"STDOUT:\n{stdout}")
            print(f"STDERR:\n{stderr}")
            # sys.exit(1) # Uncomment to exit on first error
        
        if capture_output:
            return stdout.strip(), stderr.strip(), process.returncode
        else:
            return "", "", process.returncode # Return empty strings if not capturing output

    except Exception as e:
        print(f"Exception while running command: {e}")
        # sys.exit(1) # Uncomment to exit on exception
        return "", str(e), -1

def main():
    project_root = os.getcwd()
    gitignore_path = os.path.join(project_root, ".gitignore")
    
    # 1. Ensure .gitignore exists and has correct content
    print("--- Checking and updating .gitignore ---")
    current_gitignore_content = ""
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            current_gitignore_content = f.read()
    
    if GITIGNORE_CONTENT.strip() not in current_gitignore_content:
        print(".gitignore content seems incorrect or missing. Writing correct content.")
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.write(GITIGNORE_CONTENT)
        # Stage the .gitignore file
        run_command(["git", "add", ".gitignore"])
        # Commit the .gitignore change
        run_command(["git", "commit", "-m", "chore: Update .gitignore for large files and directories"])
    else:
        print(".gitignore content is already correct.")

    # 2. Remove all currently tracked files from Git index (but keep them locally)
    # This is a crucial step to re-evaluate everything based on the new .gitignore
    print("\n--- Removing all tracked files from Git index ---")
    # We run this with ignore_errors=True because if nothing is tracked, it might error.
    # Also, we don't need to capture output here as it will be handled by add .
    run_command(["git", "rm", "--cached", "-r", "."], ignore_errors=True, capture_output=False)

    # 3. Add all files again, respecting .gitignore
    print("\n--- Adding all files again, respecting .gitignore ---")
    run_command(["git", "add", "."])
    
    # 4. Check status to see what needs to be committed
    print("\n--- Checking Git status after re-adding ---")
    stdout, stderr, returncode = run_command(["git", "status"])
    
    if "nothing to commit" in stdout and ".gitignore" not in stdout:
        print("Git status is clean. All files accounted for and ignored correctly.")
        print("No new changes to commit.")
    elif "nothing to commit" in stdout and ".gitignore" in stdout:
        print("Git status is clean. Only .gitignore was changed and committed.")
        # Push the .gitignore commit if it was the only change
        print("\n--- Pushing the .gitignore commit ---")
        for _ in range(5): # Try pushing up to 5 times
            stdout_push, stderr_push, returncode_push = run_command(["git", "push", "origin", "main"])
            if returncode_push == 0 and "Everything up-to-date" in stdout_push or "new commits" in stdout_push:
                print("Successfully pushed .gitignore commit or already up-to-date.")
                break
            else:
                print(f"Push failed. Retrying... Error: {stderr_push if stderr_push else stdout_push}")
                time.sleep(5)
        else:
            print("Failed to push .gitignore commit after multiple attempts.")
            
    else:
        print("There are changes to commit.")
        print("Current Git Status:\n", stdout)

        # 5. Commit the changes
        print("\n--- Committing changes ---")
        commit_message = "chore: Revert to clean state, ensuring .gitignore is effective removing all large files"
        run_command(["git", "commit", "-m", commit_message])

        # 6. Attempt to push repeatedly
        print("\n--- Attempting to push to origin main ---")
        max_retries = 10
        retry_delay = 10 # seconds
        for i in range(max_retries):
            stdout_push, stderr_push, returncode_push = run_command(["git", "push", "origin", "main"])
            
            if returncode_push == 0:
                if "Everything up-to-date" in stdout_push:
                    print("Push successful. Repository is up-to-date.")
                    break
                elif "new commits" in stdout_push or "Compressing objects" in stdout_push:
                    print("Push successful. New changes uploaded.")
                    break
                else:
                    # Sometimes push succeeds but the output is weird. Treat as success for now.
                    print("Push command executed, output might be unexpected but assuming success.")
                    break
            else:
                print(f"Push attempt {i+1}/{max_retries} failed.")
                print(f"Error: {stderr_push if stderr_push else stdout_push}")
                if i < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    print("Max retries reached. Push failed.")
                    print("Please check your GitHub repository manually and resolve any issues.")
                    break
        
        print("\n--- Verification ---")
        print("Please check your GitHub repository's file list NOW.")
        print("It should NOT contain any large data files or directories like 'data/', '*.nii.gz', etc.")
        print("Also, run `git status` again in your local repository.")
        
        # Final check of git status after push attempts
        print("\n--- Final Git Status Check ---")
        stdout_final, _, _ = run_command(["git", "status"])
        print(stdout_final)

if __name__ == "__main__":
    main()
