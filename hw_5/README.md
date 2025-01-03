### **Homework 5**: Asynchronous Programming and Web Scraping

#### **5.1 Asynchronous File Downloading**

- **Task**:
  1. Implement an asynchronous script for downloading images or files from one of the following websites:
     - [https://thisxdoesnotexist.com/](https://thisxdoesnotexist.com/)
     - [https://picsum.photos/](https://picsum.photos/) (preferred, as it provides unique images with each request).
  2. Allow users to specify the number of unique files to download and the target folder for saving them.
  3. Use the `aiohttp` library for asynchronous requests.
  4. Avoid using blocking code within asynchronous tasks.

---

#### **5.2 Asynchronous Real Estate Ad Scraper**

- **Task**:
  1. Develop an asynchronous scraper to collect rental property listings from one of the following websites:
     - [https://cian.ru](https://cian.ru)
     - [https://realty.yandex.ru](https://realty.yandex.ru)
     - [https://www.avito.ru](https://www.avito.ru)
  2. Gather key details from the listings, such as price, description, and links.
  3. Save the data in a format suitable for further use.
  4. Implement automatic detection of new listings.

---

#### **5.3 Telegram Bot for Ad Notifications**

- **Task**:
  1. Create a database (or use file storage) to store the information collected by the scraper.
  2. Develop a Telegram bot that allows users to:
     - Subscribe to search filters (e.g., by price, location, or other criteria).
     - Receive notifications when new relevant listings are added to the database.
  3. Package the project into a Docker container for easy deployment on a remote server.
  4. Ensure the protection of tokens and sensitive data, avoiding any leaks in public repositories.
