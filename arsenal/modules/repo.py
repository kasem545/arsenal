import os
import shutil
import subprocess
from pathlib import Path
from os.path import join, exists, expanduser


def get_repos_path():
    return join(expanduser("~"), ".arsenal", "repos")


def get_repos_file():
    return join(expanduser("~"), ".arsenal", "repos.txt")


def ensure_dirs():
    repos_path = get_repos_path()
    if not exists(repos_path):
        os.makedirs(repos_path)
    repos_file = get_repos_file()
    if not exists(os.path.dirname(repos_file)):
        os.makedirs(os.path.dirname(repos_file))


def repo_to_dirname(repo):
    return repo.replace("/", "_")


def add_repo(repo):
    ensure_dirs()
    
    if "/" not in repo:
        print(f"Invalid repo format: {repo}")
        print("Use format: owner/repo (e.g., denisidoro/cheats)")
        return False
    
    repos_path = get_repos_path()
    repo_dir = join(repos_path, repo_to_dirname(repo))
    
    if exists(repo_dir):
        print(f"Repo already exists: {repo}")
        print(f"To update, run: arsenal repo update {repo}")
        return False
    
    git_url = f"https://github.com/{repo}.git"
    print(f"Cloning {git_url}...")
    
    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", git_url, repo_dir],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Failed to clone: {result.stderr}")
            return False
    except FileNotFoundError:
        print("Git is not installed. Please install git first.")
        return False
    
    repos_file = get_repos_file()
    with open(repos_file, "a") as f:
        f.write(repo + "\n")
    
    cheat_count = len(list(Path(repo_dir).rglob("*.cheat")))
    md_count = len(list(Path(repo_dir).rglob("*.md")))
    
    print(f"Added repo: {repo}")
    print(f"Found {cheat_count} .cheat files, {md_count} .md files")
    print(f"Location: {repo_dir}")
    return True


def remove_repo(repo):
    ensure_dirs()
    
    repos_path = get_repos_path()
    repo_dir = join(repos_path, repo_to_dirname(repo))
    
    if not exists(repo_dir):
        print(f"Repo not found: {repo}")
        return False
    
    shutil.rmtree(repo_dir)
    
    repos_file = get_repos_file()
    if exists(repos_file):
        with open(repos_file, "r") as f:
            repos = [r.strip() for r in f.readlines() if r.strip() != repo]
        with open(repos_file, "w") as f:
            f.write("\n".join(repos) + "\n" if repos else "")
    
    print(f"Removed repo: {repo}")
    return True


def update_repo(repo=None):
    ensure_dirs()
    repos_path = get_repos_path()
    
    if repo:
        repos = [repo]
    else:
        repos = list_repos()
    
    if not repos:
        print("No repos to update.")
        return
    
    for r in repos:
        repo_dir = join(repos_path, repo_to_dirname(r))
        if exists(repo_dir):
            print(f"Updating {r}...")
            try:
                result = subprocess.run(
                    ["git", "-C", repo_dir, "pull", "--ff-only"],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print(f"  Updated: {r}")
                else:
                    print(f"  Failed: {result.stderr}")
            except FileNotFoundError:
                print("Git is not installed.")
                return
        else:
            print(f"  Not found: {r}")


def list_repos():
    repos_file = get_repos_file()
    if not exists(repos_file):
        return []
    
    with open(repos_file, "r") as f:
        return [r.strip() for r in f.readlines() if r.strip()]


def show_repos():
    repos = list_repos()
    repos_path = get_repos_path()
    
    if not repos:
        print("No repos installed.")
        print("")
        print("Add repos with:")
        print("  arsenal repo add denisidoro/cheats")
        print("  arsenal repo add Orange-Cyberdefense/arsenal-cheats")
        return
    
    print(f"Installed repos ({len(repos)}):")
    print("")
    for repo in repos:
        repo_dir = join(repos_path, repo_to_dirname(repo))
        if exists(repo_dir):
            cheat_count = len(list(Path(repo_dir).rglob("*.cheat")))
            md_count = len(list(Path(repo_dir).rglob("*.md")))
            print(f"  {repo}")
            print(f"    {cheat_count} .cheat, {md_count} .md files")
        else:
            print(f"  {repo} (missing)")
    print("")
    print(f"Location: {repos_path}")


def browse_repos():
    print("Popular cheatsheet repos:")
    print("")
    print("  denisidoro/cheats              - Navi's official cheatsheets")
    print("  denisidoro/navi-tldr-pages     - TLDR pages for navi")
    print("")
    print("Add with: arsenal repo add <owner/repo>")


def get_all_repo_paths():
    repos = list_repos()
    repos_path = get_repos_path()
    paths = []
    for repo in repos:
        repo_dir = join(repos_path, repo_to_dirname(repo))
        if exists(repo_dir):
            paths.append(repo_dir)
    return paths
