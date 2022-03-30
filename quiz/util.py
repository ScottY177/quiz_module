def record_quiz(quiz_id, option_id):
    with open("record.txt", "a+") as f:
        output = {}
        output["quiz_id"] = quiz_id
        output["option_id"] = option_id
        f.write(str(output) + "\n")

def check_quiz_answer(quiz_id, correct_answer):
    with open("record.txt", "r") as f:
        record = f.read().split("\n")
        for i in range(len(record)-2, -1, -1):
            # For loop from the back to check the correctness of the choice
            dictRecord = eval(record[i])
            if dictRecord["quiz_id"] == quiz_id:
                correct_option_id = f"{quiz_id}-{correct_answer}"
                assert correct_option_id == dictRecord["option_id"], f"The correct option should be: {correct_option_id}"
                break