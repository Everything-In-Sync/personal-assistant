#! /bin/env python3
from tasks import *
from knowledge import *
from vocab import *
from quotes import *
from remember import *
import random
from datetime import datetime

# Remember to run black on your code to format it

run = 0
while run == 0:

    now = datetime.now()
    taskTime = now.strftime("%m/%d/%Y")

    greetings = ["\nWhats next?", "\nYes daddy?", "\nYour command is my action"]

    class Daily:
        pass

    startOfDay = Daily()
    startOfDay.checklist = [
        "make sure storage space is empty enough to record",
        "make sure you have all screen and self recording on",
    ]
    startOfDay.breathing = "Iceman breathing technique"

    endOfDay = Daily()
    endOfDay.checklist = [
        "save files, organize folders, digitize workouts, set tomorrows tasks"
    ]

    daily = [startOfDay]

    print(random.choice(greetings))
    query = raw_input()
    if query == "category":
        print(
            "Which Category \n productivity, business, ideas, music, youtube, buy, \n "
            "sandhills geeks, personal, money, next fckn level, \n books, general, misc, money, marketing"
        )
        category = raw_input()
        for task_object in all_tasks:
            if task_object.category == category and task_object.completed == "no":
                print(task_object.task)

    elif query == "tasks":
        for task_object in all_tasks:
            if task_object.date == taskTime:
                print(task_object.task)

    elif query == "date":

        print("Which Date?")
        date = raw_input()
        for task_object in all_tasks:
            if task_object.date == date:
                print(task_object.task)
                print("Completed: " + task_object.completed)

    elif query == "start day":
        for daily_object in daily:
            print(startOfDay.checklist)
            print("\n" + startOfDay.breathing + "\n")
            print ("Tasks:")
        for task_object in all_tasks:
            if task_object.date == taskTime and task_object.completed == "no":
                print(task_object.task + "\n")
        print(random.choice(quotes))

    elif query == "end day":
        for daily_object in daily:
            print(endOfDay.checklist)

    elif query == "break":
        print(random.choice(knowledgeArray))
    elif query == "vocab":
        randomVocab = random.choice(all_vocab)
        print("\n" + randomVocab.word.upper() + "\n")
        print("Definition One: " + randomVocab.define.capitalize() + "\n")
        print("Definition Two: " + randomVocab.define2.capitalize() + "\n")
        synonyms = randomVocab.synonyms
        capitalized_synonyms = " ".join(
            [word.capitalize() for word in synonyms.split(", ")]
        )
        print("Synonyms: " + capitalized_synonyms + "\n")
        # print('Synonyms: ' + randomVocab.synonyms + '\n')
        print("Sentence: " + randomVocab.sentence.capitalize() + "\n")

    elif query == "plan":
        openPlan = open("plan.txt", "r")
        print(openPlan.read())
        openPlan.close()

    elif query == "help":
        print(
            "category, date\n"
            "start day, end day\n"
            "break, vocab, quote, plan\n"
            "take note, read notes\n"
            "new task, read new tasks\n"
            "things to remember\n"
            "end"
        )

    elif query == "take note":
        with open("note.txt", "a") as noteFile:
            print("What would you like to say? \n")
            newNote = raw_input()
            noteFile.write("\n" + "\n" + newNote)
            noteFile.close()
    elif query == "read notes":
        with open("note.txt", "r") as readNoteFile:
            notes = readNoteFile.read()
            print(notes)
            readNoteFile.close()

    elif query == "new task":
        with open("tasks.txt", "a") as taskFile:
            now = datetime.now()
            taskVariable = now.strftime("task%d%m%Y%H%M%S")
            taskFile.write(taskVariable)
            print("What is the task? \n")
            newTask = raw_input()
            taskFile.write("\n" + newTask)
            print("Category? \n")
            newTaskCategory = raw_input()
            taskFile.write("\n" + newTaskCategory)
            print("Date? \n")
            newTaskDate = raw_input()
            taskFile.write("\n" + newTaskDate)
            newTaskCompleted = "no"
            taskFile.write("\n" + newTaskCompleted + "\n")
            # task is written to file but not added as new instance or to array
            taskFile.close()
            print("done")

    elif query == "read new tasks":
        with open("tasks.txt", "r") as readTasksFile:
            data = readTasksFile.read()
            print(data)
            readTasksFile.close()
            # Now how do we add each one to a new instance of the Tasks class?

    elif query == "things to remember":
        randomRemember = random.choice(thingsToRemember)
        print(randomRemember.remember)
    elif query == "quote":
        print(random.choice(quotes))

    elif query == "end":
        run = 69
