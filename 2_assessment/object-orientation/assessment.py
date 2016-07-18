"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Encapsulation - bundling attributes and methods around each entity type better organizes code
   Abstraction - limit interaction with code to key bits of information (inputs and outputs). Hide the bulk of the logic.
   Polymorphism - ability to create logic that is reusable and not bound to a specific class


2. What is a class?
    A class is a block of code that defines a set of attributes and methods and allows the creation of objects that inherit those items from the class.

3. What is an instance attribute?
    The post-it note. A value that is assigned at the level of the instance. 

4. What is a method?
    A function that is defined within a specific class and is only available to call on objects of that class.

5. What is an instance in object orientation?
    An instance is an object that gets instantiated through the code/script. Sometimes an object can be a representation of data in a database. It can also just be defined in the code or based on user input.
    This object allows the user to interact with it.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    An instance attribute is set on the individual instance. It doesn't necessarily exist inside the class. 
    An attribute set on the class is going to be the same (at least when first initialized) for every object of that class.
    Using the example of a Car Class. You might set the class attribute of num_wheels = 4. It is most likely 4 for all cars.
    But, you would let the color be set at the instance level, because most cars vary in color.
    num_wheels is true for all cars, making it better for a class attribute.
    color is something that each car has, but isn't the same for every car. So it would be part of the class, but set at the instance level.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A student"""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A Question with answer"""
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ Prompt user for answer to question.

            Return True/False based on correct_answer"""

        print "Answer True or False"
        answer = raw_input(self.question + "\n")

        return answer.lower() == self.correct_answer.lower()


class Exam(object):
    """A named Exam containing list of questions."""
    def __init__(self, name, questions=[]):
        self.name = name
        self.questions = questions

    def add_question(self, question, correct_answer):
        """ Create and add a Question object to the exam's list of questions."""
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

        return self.questions

    def administer(self):
        """ Administer the questions and tally score."""

        print "num questions", len(self.questions)
        score = float(0.0)
        for question in self.questions:
            answer = question.ask_and_evaluate()
            if answer:
                score += 1
        
        score = score / len(self.questions)

        # test if exam is quiz. if so only return pass/fail
        try:
            if self.is_quiz:
                if score >= .5:
                    return True
                else:
                    return False
        except AttributeError:
            return score


class Quiz(Exam):
    """docstring for Quiz"""
    
    is_quiz = True

    def __init__(self, name):
        super(Quiz, self).__init__(name)
        self.name = name
        

def take_test(exam, student):
    """For a student, administer specified exam."""

    student.score = exam.administer()

    return student.score

def example():
    """ Provide workflow template for creating exam, student and administer test."""

    #create an exam
    exam = Exam("test")
    # prepopulate two questions if exam doesn't already exist
    if len(exam.questions) == 0:
        exam.questions.append(Question("What color is sky", "blue"))
        exam.questions.append(Question("In what month does Christmas fall.", "December"))
    # create a student
    student = Student("Alice", "Walker", "1111 Main")
    #administer the test
    result = exam.administer()

    return result




        
        