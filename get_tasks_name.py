from datasets import load_dataset

dataset = load_dataset("r1v3r/auto_0207_bug_updated",split='train')
tasks = []
for example in dataset:
    tasks.append(example['instance_id'])
    print(example['instance_id'])

with open('tasks.txt', 'w') as f:
    for task in tasks:
        f.write(task + '\n')