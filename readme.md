
# Us-chat

Us-chat is a real-time chat website built using Django, leveraging WebSocket technology for smooth and instant messaging. Users can create and join rooms to engage in conversations with other participants. All messages from the conversations are saved, providing a persistent chat history.

## Features

- Real-time messaging using WebSocket
- Room creation and joining
- Persistent chat history
- Robust authentication

## Technologies Used

- Django
- Channels (for WebSocket support)
- Redis (for message caching)
- HTML, CSS, JavaScript (for the frontend)
  

## Getting Started

To run the Us-chat application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Us-chat.git
   cd Us-chat
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and visit `http://localhost:8000` to access the Us-chat application.

## Usage

1. Open the Us-chat website.
2. Create a new account or log in.
3. Create or join a room.
4. Start chatting with other participants in real-time.

## Sample

### Login
![Screenshot 2023-12-24 113151](https://github.com/SIdR4g/Us-Chat/assets/78850085/85d744dc-fb22-4844-a053-62b817fed9a8)

### Room Options
![Screenshot 2023-12-24 113215](https://github.com/SIdR4g/Us-Chat/assets/78850085/82b6355b-c5c0-443d-8a19-964277c06d84)

### Create Room
![Screenshot 2023-12-24 113225](https://github.com/SIdR4g/Us-Chat/assets/78850085/8ee53cca-ae1b-435a-bd7c-27b2a3c85f7e)

### Join Room
![Screenshot 2023-12-24 113315](https://github.com/SIdR4g/Us-Chat/assets/78850085/6734baa6-d907-48df-a0d8-e3a22536dd0f)

### Messaging Interface
![Screenshot 2023-12-24 113902](https://github.com/SIdR4g/Us-Chat/assets/78850085/ec32d74f-264b-492a-b063-b2be8a6e0173)

## Contributing

If you'd like to contribute to Us-chat, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or issues, please contact [siddyant34@gmail.com].


