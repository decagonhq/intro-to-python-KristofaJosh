## Introduction to Python

Github Classroom Assignment Link : https://classroom.github.com/a/oUE_Og9m

Tasks Definition : https://docs.google.com/document/d/1V1gYEKLtOPYzZL7F9koaDVdgIlOXl_ALspjyzOZJN7Q/edit?usp=sharing


## Understanding Solid Principles
The idea behind the **Solid** principle is to manage dependency.
_1._ **S**RP => Illustrates having methods that perform single responsibility. The idea is to have methods that perform specific functions to their creation
Eg: A function meant to display error messages should not do anything other than that.

_2._**O**CP => When creating a system or method, build it in such a way that it can be extended rather than modified. OCP is a form of abstraction in OOD.

_3._**L**SP => the ability to replace any instance of a parent class with an instance of one of its derived classes without breaking the code

_4._**I**SP => simply says that only methods needed by a derived class should be available from the parent class. For interfaces, it is better to have many interface with fewer methods than have Fewer Interfaces with many methods in them so that they would be no need for a new entire class creation

_5._**D**IP => high level functions should not implement low implementation but both should depend on abstraction. This is to reduce the impact of changes
