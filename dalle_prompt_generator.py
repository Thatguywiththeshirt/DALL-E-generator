import json

import random


def load_data(filename):

	try:

		with open(filename, 'r') as file:

			data = json.load(file)

		return data

	except FileNotFoundError:

		print(f"Error: {filename} not found.")

		return None

	except json.JSONDecodeError:

		print(f"Error: Invalid JSON in {filename}.")

		return None


def generate_dalle_prompt(data):
    orientation = random.choice(data['orientations'])
    artist = random.choice(data['artists'])
    object_ = random.choice(data['objects'])
    medium = random.choice(data['mediums'])
    color = random.choice(data['color'])

    return f"A {orientation} {medium} in the style of {artist}, featuring a {object_} with a {color} color scheme."




def main(data, num_prompts):

	for _ in range(num_prompts):

		print(generate_dalle_prompt(data))


if __name__ == '__main__':

	data = load_data('dalle_prompt_data.json')

	if data:

		try:

			num_prompts = int(input('Enter the number of prompts to generate: '))

			if num_prompts < 1:

				raise ValueError

			main(data, num_prompts)

		except ValueError:

			print("Error: Please enter a positive integer.")
