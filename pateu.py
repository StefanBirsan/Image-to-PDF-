import os
from PIL import Image

def menu():
    print('[1] Create one PDF from one image')
    print('[2] Combine more PDFs')
    print('[3] Exit')
    choice = int(input('Enter your choice: '))
    return choice

input_dir = './PDFS'
images = []

for file in os.listdir(input_dir):
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
        image = Image.open(os.path.join(input_dir, file))
        images.append(image)

choice = menu()

if choice == 1:
    # Save the wanted image as a PDF file
    print('What is the name of the image?')
    imgname = input()

    # Get the filename from the user
    print('What do you want the file to be named?')
    filename = input()

    # Save the image as a PDF file
    image = Image.open(os.path.join(input_dir, imgname))
    image.save(filename + '.pdf', 'PDF')
    
elif choice == 2:
    # Print all image filenames
    print('Here are all the image filenames:')
    for i, img in enumerate(images):
        print(f'{i+1}. {img.filename}')

    # Get the order from the user
    print('Enter the filenames in the order you want them to appear in the PDF, enclosed in quotes if they contain spaces and using spaces between file names:')
    order = input().strip().split('" ')
    order = [filename.replace('"', '') for filename in order]

    # Open the images in the specified order
    ordered_images = [Image.open(os.path.join(input_dir, filename)) for filename in order]

    # Get the filename from the user
    print('What do you want the file to be named?')
    filename = input()

    # Save all images in one PDF file
    ordered_images[0].save(filename + '.pdf', 'PDF', save_all=True, append_images=ordered_images[1:])

elif choice == 3:
    print('Exiting the program.')
    exit()
else:
    print('Invalid choice.')
