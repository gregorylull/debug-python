"""
Sometimes you have a large amount of data you are looping through,
you do not want to stop on every single item.

So you add a conditional!
- on the leftside of the number line, right click and 'add conditional breakpoint'

"""
import data 
persons = data.get_persons()


def get_BMI(person):
    weight = person['weight']
    height = person['height']

    return weight / (height * height)

def main():
    BMIs = []
    for person in persons: 
        BMIs.append(get_BMI(person))

    return BMIs

if __name__ == '__main__':
    results = main()
    print(results)

