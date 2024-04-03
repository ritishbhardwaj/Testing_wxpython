import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# # Execute the SELECT query to retrieve the image data
# cursor.execute("create table activity ( id int primary key, photoname str, photo BLOB  ); ")

# # Fetch the result (assuming there's only one image to retrieve)
# # image_data = cursor.fetchone()[0]

# # Write the binary image data to a file
# # with open('retrieved_image.png', 'wb') as f:
#     # f.write(image_data)

# # Close the cursor and connection
# cursor.close()
# conn.close()

from PIL import ImageGrab
import io

# Take a screenshot
screenshot = ImageGrab.grab()
screenshot.save('ss/screenshot.png')
# Convert the screenshot image into bytes
screenshot_bytes = screenshot.tobytes()
# print(screenshot_bytes)
# Create a io.BytesIO object and write the bytes data into it
# bytes_io_object = io.BytesIO()
# bytes_io_object.write(screenshot_bytes)



# //implement taking some data
match (int(input("input=="))):
    case 1:
        query = "insert into activity values(1,'simple_ss1',?)"
        cur.execute(query,(screenshot_bytes,))
        conn.commit()

        # // insert cmd which insert above data in db
        pass
    case 2:
        query  = "Select * from activity"
        data = cur.execute(query)

        output = data.fetchall()
        print(output[0][1])
        binary_data= output[0][2].getvalue()
        print(binary_data)
        with open('new_img.png', 'wb') as f:
            f.write(binary_data)

        # // show cmd which insert above data in db
        pass
    case 3:
        # // delete
        pass
    case 4:
        
        pass
    case 5:
        pass



'''
tuple 
(1,)
(1,)

[1]
[1,]

'''