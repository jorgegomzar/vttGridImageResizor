from PIL import Image

def main():
	while True:
		pic_path = input('\n- Ubicación de la imagen: ')
		if pic_path == '':
			break
		image = Image.open(pic_path)
		size = image.size

		matrix = (int(input('- Rows: ')), int(input('- Cols: ')))
		wc = int(input('- Width per cell: '))

		print('Old size: {} x {}'.format(size[0], size[1]))
		print('New size: {} x {}'.format(matrix[0]*wc, matrix[1]*wc))

		if 'n' in input('Ok? (Y/n) default Y: '):
			break
		new_image = image.resize((matrix[0]*wc, matrix[1]*wc))
		image.close()
		new_image.save(pic_path)

if __name__ == "__main__":
	main()
