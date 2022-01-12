from todo import *
from note import *
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

    # def test_note_class_user(self)
        

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


