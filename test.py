from todo import *
from note import *
from user import *
import unittest
import pendulum
class TodoTest(unittest.TestCase):

    def test_topic_class(self):
        topic = Topic()
        topic.setTopic("Hello")
        self.assertEqual(topic.getTopic(), "Hello")
        topic.setDescription("I love you")
        self.assertEqual(topic.getDescription(), "I love you")

    def test_todo_class_order(self):
        todo = Todo()
        todo.setOrderList(1)
        self.assertEqual(todo.getOrderList(), 1)
        with self.assertRaises(TypeError):
            todo.setOrderList("hi")
            todo.setOrderList(True)

    def test_todo_class_done(self):
        todo = Todo()
        todo.setDone(True)
        self.assertTrue(todo.getDone())
        with self.assertRaises(TypeError):
            todo.setDone("hi")
            todo.setDone(1)

    def test_todo_class_date(self):
        todo = Todo()
        todo.setDate("2001/1/2")
        self.assertEqual(todo.getDate(), pendulum.from_format("2001/1/2", "YYYY/MM/DD"))
        self.assertEqual(todo.getDateString(), "2001-01-02")
        with self.assertRaises(ValueError):
            todo.setDate("2001/1-2")
            todo.setDate("2001/21/2")
            todo.setDate("2001/11/32")

    def test_user_class(self):
        user = User()
        user.changeName("ong")
        self.assertEqual(user.getName(), "ong")
        with self.assertRaises(TypeError):
            user.changeName(123)
            user.changeName(True)
        
    def test_note_class_json(self):
        note = Note()
        note.createTodo("hello", "hi", "2001/1/2")
        todoList = note.getTodos()
        self.assertEqual(len(todoList), 1)
        self.assertEqual(todoList[0]['topic'], "hello")
        self.assertEqual(todoList[0]['desc'], "hi")
        self.assertEqual(todoList[0]['endDate'], "2001-01-02")

        note.toJson()
        data = note.loadJson()
        self.assertEqual(list(data.keys()), ["user1"])
        self.assertEqual(data["user1"][0]['topic'], "hello")
        self.assertEqual(data["user1"][0]['desc'], "hi")
        self.assertEqual(data['user1'][0]['endDate'], "2001-01-02")

        note.createTodo("hello2", "hi2", "2001/1/3")
        self.assertEqual(len(todoList), 2)
        self.assertEqual(todoList[1]['topic'], "hello2")
        self.assertEqual(todoList[1]['desc'], "hi2")
        self.assertEqual(todoList[1]['endDate'], "2001-01-03")

        note.changeUser("ong")
        self.assertEqual(note.user.getName(), "ong")
        note.createTodo("world", "yeah", "2022/2/3")
        todoList = note.getTodos()
        self.assertEqual(len(todoList), 1)
        self.assertEqual(todoList[0]['topic'], "world")
        self.assertEqual(todoList[0]['desc'], "yeah")
        self.assertEqual(todoList[0]['endDate'], "2022-02-03")

        note.toJson()
        data = note.loadJson()
        self.assertEqual(list(data.keys()), ["user1", "ong"])
        self.assertEqual(data["ong"][0]['topic'], "world")
        self.assertEqual(data["ong"][0]['desc'], "yeah")
        self.assertEqual(data['ong'][0]['endDate'], "2022-02-03")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


