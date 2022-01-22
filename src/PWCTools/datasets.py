from importlib import resources

def get_cars():
    """Get path to example cars text file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    .. [1] Cars dataset.
    """
    with resources.path("PWCTools.data", "cars.txt") as f:
        data_file_path = f
    return data_file_path