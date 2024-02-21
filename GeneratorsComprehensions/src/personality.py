import random
import unittest

CLASS_NAME = 'Turret'
PERSONALITY_TRAITS = ['neuroticism', 'openness',
                      'conscientiousness', 'extraversion', 'agreeableness']
ACTIONS = ['shoot', 'search', 'talk']


def turrets_generator() -> object:
    def shooting():
        print("Shooting")

    def searching():
        print("Searching")

    def talking():
        print("Talking")

    def get_number():
        total = 100
        for i in range(5):
            if i < 4:
                rand = random.randint(0, total)
                total -= rand
            else:
                rand = total
            yield rand

    turret_class = type(
        CLASS_NAME,
        (object, ),
        {
            ACTIONS[0]: shooting,
            ACTIONS[1]: searching,
            ACTIONS[2]: talking
        } | {
            key: number
            for key, number in zip(PERSONALITY_TRAITS, get_number())
        }
    )
    return turret_class


class PersonalityTests(unittest.TestCase):
    def get_sum(self, obj):
        total = obj.neuroticism
        total += obj.openness
        total += obj.conscientiousness
        total += obj.extraversion
        total += obj.agreeableness
        return total

    def check_similarity(self, obj, obj2):
        flag = True
        flag = False if obj.neuroticism != obj2.neuroticism else flag
        flag = False if obj.openness != obj2.openness else flag
        flag = False if obj.conscientiousness != obj2.conscientiousness \
            else flag
        flag = False if obj.extraversion != obj2.extraversion else flag
        flag = False if obj.agreeableness != obj2.agreeableness else flag
        return flag

    def test1(self):
        obj1 = turrets_generator()
        obj2 = turrets_generator()

        self.assertEqual(100, self.get_sum(obj1))
        self.assertEqual(100, self.get_sum(obj2))
        self.assertFalse(self.check_similarity(obj1, obj2))


if __name__ == "__main__":
    unittest.main()
