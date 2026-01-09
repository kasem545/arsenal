# apt
## apt - Update package lists
sudo apt update

## apt - Upgrade all installed packages to their latest versions
sudo apt upgrade

## apt - Install a package
sudo apt install  <package-name>

## apt - Remove a package
sudo apt remove  <package-name>

## apt - Search for a package
apt search  <package-name>

## apt - Show information about a package
apt show  <package-name>

## apt - Clean up unused packages and dependencies
sudo apt autoremove

## apt - Clean up downloaded package files
sudo apt clean

## apt - Fix broken dependencies
sudo apt --fix-broken install

## apt - Purge a package along with its configuration files
sudo apt remove --purge  <package-name>



# npm

## npm - List all local packages
npm list

## npm - List all globally installed packages
npm list -g

## npm - Check a specific package's version and dependency details
npm list  <package-name>

## npm - Install a package locally
npm install  <package-name>

## npm - Install a package globally
npm install -g  <package-name>

## npm - Uninstall a local package
npm uninstall  <package-name>

## npm - Uninstall a global package
npm uninstall -g  <package-name>

## npm - Update a specific package
npm update  <package-name>

## npm - Update a global package
npm update -g  <package-name>

## npm - Run security audits on installed packages
npm audit

## npm - Automatically fix vulnerabilities in installed packages
npm audit fix


# uv

## uv - Install package from PyPI
```
uv tool install <package-name>
```
## uv - Install from GitHub
```
uv tool install git+<github-repo-url>
```
## uv - Upgrade all tools
```
uv tool upgrade --all
```
## uv - List installed tools
```
uv tool list
```

## uv - inject missing modules
```
uv add --script <script-path> <package-name>
```

# pipx

## pipx - Install a package
pipx install  <package-name>

## pipx - Uninstall a package
pipx uninstall  <package-name>

## pipx - List installed packages
pipx list

## pipx - Upgrade a package
pipx upgrade  <package-name>

## pipx - Upgrade all packages
pipx upgrade-all

## pipx - Installing the latest version from a repo 
pipx install git+<github-repo-url>