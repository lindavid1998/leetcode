def solve(width, height, num_blocks, grid):
	block_positions = get_block_positions(grid)

	for block, positions in block_positions.items():
		if can_move_block(grid, width, block, positions):
			return int(block)

	return -1


def get_block_positions(grid):
	blockToPositions = {}  # block_id -> set() of [i, j]

	for i, row in enumerate(grid):
		for j, col in enumerate(row):
			current = grid[i][j]
			if current == 'x' or current == '.':
				continue
			if current not in blockToPositions:
				blockToPositions[current] = set()
			blockToPositions[current].add((i, j))

	return blockToPositions

def can_move_block(grid, width, block_num, positions):
	# returns True if block represented by positions set can be moved off the
	# board to the right without collisions

	# while positions is not empty
	while positions:
		# init next positions set
		next_positions = set()
		
		# for each position
		for i, j in positions:
			# shift it to the right
			j += 1

			# if at edge
			if j == width:
				continue

			# if it collides with 'x' or another block (diff num)
			if grid[i][j] == 'x' or (grid[i][j].isnumeric() and grid[i][j] != block_num):
				return False
			
			# append new position to next positions set
			next_positions.add((i, j))

		# overwrite positions with next positions
		positions = next_positions
		
	return True

test_case_1 = {
	'case': 1,
	'grid':  [
			'xxxxx',
			'x...1',
			'xxxxx'
		],
	'num_blocks': 1,
	'ans': [1]
}

test_case_2 = {
	'case': 2,
	'grid': [
		'xxxxx',
		'x.122',
		'xxxxx'
	],
	'num_blocks': 2,
	'ans': [2]
}

test_case_3 = {
	'case': 3,
	'grid': [
		'xxxxx',
		'x.2.1',
		'x.2.1',
		'x.2.1',
		'xxxxx'
	],
	'num_blocks': 1,
	'ans': [1]
}

test_case_4 = {
	'case': 4,
	'grid': [
		'xxxxxx',
		'x4....',
		'x1.2.3',
		'x33333',
		'xxxxxx'
	],
	'num_blocks': 4,
	'ans': [3, 4]
}

test_case_5 = {
	'case': 5,
	'grid': [
		'xxxxxx',
		'x1...5',
		'x.2..5',
		'x..3.5',
		'x...45',
		'x....5',
		'xxxxxx'
	],
	'num_blocks': 4,
	'ans': [5]
}


all_cases = [
	test_case_1,
	test_case_2,
	test_case_3,
	test_case_4,
]

for test_case in all_cases:
	grid = test_case['grid']
	height = len(grid)
	width = len(grid[0])

	res = solve(width, height, test_case['num_blocks'], grid)
	ans = test_case['ans']

	try:
		assert res in ans
	except:
		print(f"Failed test case {test_case['case']}, got {res} but expected {ans}") 
