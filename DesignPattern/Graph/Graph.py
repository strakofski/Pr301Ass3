from Graph.IGraph import *

import plotly as plt
import plotly.graph_objs as go


class GraphView:
    __Graph = None

    def get_builder(self, builder):
        self.__Graph = builder

    def do_make_graph(self, graph):
        graph = Graph()
        graph_type =self.__Graph.get_graph_type()
        graph.do_build_graph(graph_type)

class Graph(metaclass=ABCMeta):

    def __init(self, database):
        self.database = database

    @abstractmethod
    def do_build_graph(self, data):
        pass

    @abstractmethod
    def do_display_graph(self, graph):
        pass


    @staticmethod
    def append_sql(self, sql):
        database = self.database
        database.execute_sql(sql)
        return database.cursor.fetchall()



class SalesByGenderGraph(Graph):

    #to re think :-/


    def __init__(self, database):
        self.graph_data = None
        self.database =  database
        self.graph_data1 = []
        self.graph_data2 = []

    def get_data(self,field, val, min, max):
        formatted_sql = """SELECT * FROM employee WHERE {0} = {1} AND Salary BETWEEN {2} AND {3}""".format(
            field, val, min, max
        )

        return formatted_sql


    def do_build_graph(self, data):
        gender = []
        sales = []
        graph_data = [plt.Bar(
            x=gender,
            y=sales,
        )]

        format_graph = plt.Layout(
            title="Gender vs Sale",
            x= dict(title="Gender"),
            y= dict(title="Sales")
        )
        self.graph_data = plt.Figure(data=graph_data, layout=format_graph)


    def do_display_graph(self, graph):
        plt.plot(self.graph_data)


class EmployeesByGenderGraph(Graph):

    def __init__(self, database):
        self.graph_data = None
        self.database = database

    def do_display_graph(self, graph):
       plt.plot(self.graph_data)

    def get_data(self, data):
        formated_sql = """SELECT * FROM employee WHERE gender = '{0}'""".format(data)
        return len(self.append_sql(formated_sql))

    def do_build_graph(self, data):
        male_count = self.get_data('m')
        female_count = self.get_data('f')

        self.graph_data = {
            'data': [{'labels': ['Male', 'Female'],
                      'values': [male_count, female_count],
                      'type': 'pie'}],

            'layout': {
                'title': 'Number of Employees by Gender'
                }
        }

class age_verse_salary_graph(Graph):

    #to fix or look at again :-/

    def __init__(self, database):
        self.graph_data = None
        self.database = database
        self.graph_data1, self.graph_data2, self.graph_data3, self.graph_data4 = []

    def do_display_graph(self, graph):
        plt.plot(self.graph_data)

    def get_age_between(self, min, max):
        formatted_sql = """SELECT * FROM salary WHERE age BETWEEN '{0}' AND '{1}'""".format(min, max)
        return

    def get_salary_by_between(self, field, val, min, max):
        formatted_sql = """ELECT * FROM employee WHERE {0} = {1} AND Salary BETWEEN {2} AND {3}""".format(
            field, val, min, max
        )
        return formatted_sql

    def get_data(self, field, val, min, max):
        data1, data2, data3, data4 = []

        self.graph_data1.append(self.get_salary_by_between('age', 26, 0, 125))
        self.graph_data1.append(self.get_salary_by_between('age', 26, 126, 150))
        self.graph_data1.append(self.get_salary_by_between('age', 26, 151, 175))
        self.graph_data1.append(self.get_salary_by_between('age', 26, 176, 200))

        self.graph_data2.append(self.get_salary_by_between('age', 26, 0, 125))
        self.graph_data2.append(self.get_salary_by_between('age', 26, 126, 150))
        self.graph_data2.append(self.get_salary_by_between('age', 26, 151, 175))
        self.graph_data2.append(self.get_salary_by_between('age', 26, 176, 200))

        self.graph_data3.append(self.get_salary_by_between('age', 26, 0, 125))
        self.graph_data3.append(self.get_salary_by_between('age', 26, 126, 150))
        self.graph_data3.append(self.get_salary_by_between('age', 26, 151, 175))
        self.graph_data3.append(self.get_salary_by_between('age', 26, 176, 200))

        self.graph_data4.append(self.get_salary_by_between('age', 26, 0, 125))
        self.graph_data4.append(self.get_salary_by_between('age', 26, 126, 150))
        self.graph_data4.append(self.get_salary_by_between('age', 26, 151, 175))
        self.graph_data4.append(self.get_salary_by_between('age', 26, 176, 200))

    def do_build_graph(self, data):
        age_data =  []
        salary_data = []
        graph_data = [go.Bar(
            x=age_data,
            y=salary_data,
            name= "Age vs Salary"

        )]
        format_graph = plt.Layout(title="Salary Vs Age",x = dict(title="Age"),
        y = dict(title="Salary")
        )
        self.graph_data = go.Figure(data=graph_data, layout=format_graph)


class BmiPieGraph(Graph):
    def __init__(self, database):
        self.graph_data = None
        self.database = database

    def do_display_graph(self, graph):
        plt.plot(self.graph_data)

    def get_data(self, data):
        formated_sql = """SELECT * FROM employee WHERE bmi = '{0}'""".format(data)
        return len(self.append_sql(formated_sql))

    def do_build_graph(self, data):
        uw = self.get_data('Underweight')
        norm = self.get_data('Normal')
        ow = self.get_data('Overweight')
        obs = self.get_data('Obesity')

        self.graph_data = {
            'data': [{'labels': ['Underweight', 'Normal', 'Overweight', 'Obese'],
                      'values': [uw, norm, ow, obs],
                      'type': 'pie'}],

            'layout': {
                'title': 'Employee BMI'
            }
        }