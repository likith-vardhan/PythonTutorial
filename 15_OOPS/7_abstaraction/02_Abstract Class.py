# 🔹 4. Abstract Class
# ✅ Definition

# A class that cannot be instantiated and contains abstract methods


from abc import ABC, abstractmethod

class MyClass(ABC):
    @abstractmethod
    def my_method(self):
        pass



#     🔹 7. Why Abstract Classes?
# Enforce rules for child classes
# Ensure method implementation
# Provide common structure