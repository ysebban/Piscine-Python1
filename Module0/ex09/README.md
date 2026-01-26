+ + + My first Python package
    * you will find here, some of the function we created and implented in previous exercice
+ + Commands list to launch the package
    * 1 go to directory ex09
        `cd ex09`
    * 2 install .venv 
        `python3 -m venv .venv`
        `source .venv/bin/activate`
    * 3 set_up dist/ environement
        `python -m pip install --upgrade build`
        `python -m build`
    * 4 launch the package 
        `pip install ./dist/ft_package-0.0.1.tar.gz`
        Or
        ` pip install ./dist/ft_package-0.0.1-py3-none-any.whl`
    * 5 finally call the package from anywhere
        `import ft_package`

+ + Commands list to test the package from pip
    * Show all installed packages
        `pip list`
    * Show detail about the package
        `pip show -v ft_package`
    * verify the package is importable
        `python -c "import ft_package"`
    * test one function direclty
        `python -c "from ft_package import NULL_not_found; print(NULL_not_found(None))"`
    * show help
        `python -c "import ft_package; help(ft_package)"`
        `python -c "from ft_package import ft_filter; help(ft_filter)"`

+ + Commands list to erase package
    * unistall package from venv
    `pip uninstall ft_package`
    * stop venv
    `deactivate`
    * erase all data
    `rm -rf venv dist build *.egg-info`