import importlib
from typing import Optional


class ModuleLoader:
    """
    ModuleLoader is a utility class that provides methods to dynamically load modules and classes from the given module.

    Parameters:
        None

    Returns:
        None

    Example:
        >>> ModuleLoader.import_module_by_name("os")
        <module 'os' from '/usr/lib/python3.8/os.py'>
    """

    @staticmethod
    def import_module_by_name(module_name: str, prefix: Optional[str] = None) -> object:
        """
        Dynamically imports a module by name.

        Parameters:
            module_name (str): The name of the module to import.
            prefix (Optional[str]): An optional prefix to add to the module name.

        Returns:
            object: The imported module.

        Example:
            >>> ModuleLoader.import_module_by_name("os")
            <module 'os' from '/usr/lib/python3.8/os.py'>
        """
        try:
            if prefix is not None:
                module_name = prefix + module_name
            return importlib.import_module(module_name)
        except ImportError:
            print(
                f"Module {module_name} could not be imported. Make sure it's installed and available on your PYTHONPATH."
            )

    @staticmethod
    def import_module_by_path(module_path: str) -> object:
        """
        Dynamically imports a module by path.

        Parameters:
            module_path (str): The path of the module to import.

        Returns:
            object: The imported module.

        Example:
            >>> ModuleLoader.import_module_by_path("/usr/lib/python3.8/os.py")
            <module 'os' from '/usr/lib/python3.8/os.py'>
        """
        try:
            return importlib.import_module(module_path)
        except ImportError:
            print(
                f"Module {module_path} could not be imported. Make sure it's installed and available on your PYTHONPATH."
            )

    @staticmethod
    def load_class_from_module(
        module_name: str, class_name: str, prefix: Optional[str] = None
    ) -> object:
        """
        Dynamically loads a class from a module.

        Parameters:
            module_name (str): The name of the module containing the class.
            class_name (str): The name of the class to load.
            prefix (Optional[str]): An optional prefix to add to the module name.

        Returns:
            object: The loaded class.

        Example:
            >>> ModuleLoader.load_class_from_module("os", "path")
            <class 'posixpath._Path'>
        """
        module = ModuleLoader.import_module_by_name(module_name, prefix)
        if module is not None:
            return getattr(module, class_name)
        else:
            return None

    @staticmethod
    def execute_function_from_module(
        module_name: str, function_name: str, prefix: Optional[str] = None
    ) -> object:
        """
        Dynamically executes a function from a module.

        Parameters:
            module_name (str): The name of the module containing the function.
            function_name (str): The name of the function to execute.
            prefix (Optional[str]): An optional prefix to add to the module name.

        Returns:
            object: The result of the executed function.

        Example:
            >>> ModuleLoader.execute_function_from_module("os", "getcwd")
            '/Users/alansynn'
        """
        module = ModuleLoader.import_module_by_name(module_name, prefix)
        if module is not None:
            return getattr(module, function_name)()
        else:
            return None
