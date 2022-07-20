def recover_methods(cls):
    if hasattr(cls, "_from_dict"):
        setattr(cls, "from_dict", getattr(cls, "_from_dict"))
    if hasattr(cls, "_to_dict"):
        setattr(cls, "to_dict", getattr(cls, "_to_dict"))
    return cls
