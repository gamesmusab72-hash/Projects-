# class something:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age 
    
#     @property 
#     def __str__(self):
#         return f"the name is {self.__name}"
# person = something
# person.name = "Seraj"

# print(person.name )


# class EntrollCourse:
#     def __init__(self, course_name, credit_hours):
#         self.name = course_name
#         self.hours = credit_hours
#     def get_course_details(self):
#         return f"course name: {self.name} and credit hours are {self.hours}"
# class Student:
#     def __init__(self,name, student_ID, obj_course):
#         self.name = name
#         self.stuID = student_ID
#         self.enrolled = obj_course
#     def get_student_schedule(self):
#         return f"The student {self.name} with the ID {self.stuID} has enrolled in the following courses: {self.enrolled.get_course_details()}"

# course1 = EntrollCourse ("Math" , 15)
# student1 = Student("Musan", "6322", course1)


# class Author:
#     def __init__(self, name):
#         self.name = name
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author 
#     def get_details(self):
#         return f"Book: '{self.title}' written by {self.author.name}"
# my_author = Author("Esraa ahmed")
# my_book = Book("OOP", my_author)
# print(my_book.get_details())


# # Another example:
# class Professor:
#     def __init__(self, name, specialty):
#         self.name = name
#         self.specialty = specialty
#     def __str__(self):
#         return f"Professor {self.name} (Specialty: {self.specialty})"
# class Department:
#     def __init__(self, dept_name):
#         self.dept_name = dept_name
#         self.professors = []
#     def add_professor(self, prof):
#         self.professors.append(prof)
#     def show_staff(self):
#         print(f"Department: {self.dept_name}")
#         for p in self.professors:
#             print(f"- {p}")
# prof1 = Professor("Dr. Ahmed", "AI")
# prof2 = Professor("Dr. Sara", "Data Science")
# it_dept = Department("Information Technology")
# it_dept.add_professor(prof1)
# it_dept.add_professor(prof2)
# it_dept.show_staff()


class Meal:
    def __init__(self, meal_type):
        self.__meal_type = meal_type  
    
    @property 
    def meal_type(self):
        return self.__meal_type
    
    @meal_type.setter 
    def meal_type(self, new):
        self.__meal_type = new


class Order:
    def __init__(self, order_id, meal_type):
        self.ordid = order_id
        self.mealorder = Meal(meal_type)
    
    def show_details(self):
        return f"Order ID: {self.ordid}, Meal: {self.mealorder.meal_type}"


class DeliveryOrder(Order):
    def __init__(self, order_id, meal_type, delivery_time):
        super().__init__(order_id, meal_type)   
        self.time = delivery_time
    
    def show_details(self):
        return f"Delivery Order ID: {self.ordid}, Meal: {self.mealorder.meal_type}, Delivery Time: {self.time}"



order1 = Order(101, "Pizza")
print(order1.show_details())

delivery1 = DeliveryOrder(202, "Burger", "18:30")
print(delivery1.show_details())
