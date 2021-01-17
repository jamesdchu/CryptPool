## Inspiration
Crowdfunding sites today are seriously flawed: fees, limited currencies, and a lack of support for many countries. These inconveniences prevent many people from donating to a cause.

We wanted to create a **global humanitarian solution**, allowing people from all around the world to donate to **anyone**, **anywhere** they want. This will allow important fundraisers to gain a global audience and secure more substantial funds.

We decided to use the Stellar SDK because it supports **many different types of currencies**, making it more convenient than ever for a user to donate to a fundraiser. We also chose **Stellar** because of their extremely fast verification process, only taking 3-5 seconds per transaction, which allows users to instantly move money globally, regardless of their fiat currency/banks.

CryptPool gives its users the ability to spend their assets where it matters to them, and gives others the tools to showcase their idea to a global audience for a chance for them to get the finances to make their dreams a reality. This platform can also act as a place for people to bring awareness to issues, through **crowdfunding campaigns**. People can see the support shown, giving them hope for problems in their own lives, and chipping in to create social change for the better.

## What it does
Users are able to donate to fundraisers that they believe in or want to help fund. These fundraisers can range from start-up costs to medical emergencies for loved ones. By using Stellar we can create a platform that uses all types of currencies, digital or physical. Current fundraising platforms do not support cryptocurrency, something that more and more people are inclined to use, instead of current world currencies. 

Users will also be able to **create a fundraiser** if they need to. Using our intuitive fundraiser creator, users will be able to categorize their fundraiser, add descriptions, and include pictures in order to attract the maximum number of supporters. Categorizing fundraisers will also allow users to target a specific audience or find related fundraisers they want to support.

With CryptPool’s **history** page, users will be able to review their previous donations and track their current fundraisers. This allows them to keep track of their assets, and see how well a fundraiser is doing.

## How we built it
Immediately after discussing and outlining how we wanted our website to work, we went to work. First off, we set up our GitHub repository with the essential files and planned out deadlines/goals for our project to ensure an efficient and productive timeline. We also used a LiveShare connection such that all four of us could work simultaneously off of one device. For our front end, we created HTML, CSS, and JavaScript files for each page that we wanted to put in our project. We used **Jinja** to update each page with new information and to automate the display of it. 

For our backend, we used MongoDB, Flask, and Stellar SDK. We decided to use a **Document Oriented DBMS** to organize and store our data for easy access and usage which was very helpful in the history page and for showing previous donations. We also encrypted all sensitive information using **bcrypt** to improve our security. 

To process all transactions, we used the **Stellar SDK**, which consisted of choosing a supported asset and how much to send. Attached to each transaction, we used our unique IDs for each user and fundraiser to document the details of each donation. In conjunction with our other backend technologies, we were able to retrieve and store data efficiently, allowing for quick loading times. 

## Challenges we ran into
Starting off, coming up with an effective real-world idea was difficult, as we were attempting to create a completely new idea that could leverage Stellar to its fullest capabilities. This meant we had to learn all about Stellar. This included what it was, some of its applications, and how to implement it in our code so that it is fully integrated with our **full-stack web application**. Another issue we had was effectively organizing our database such that we could query our desired information (e.g. past donations) and show it on the frontend (decided to use Jinja!). 

## Accomplishments that we're proud of
CryptPool was one of our most ambitious projects yet and creating a functioning and successful prototype is something that we’re proud of. Working long hours (with lots of caffeine!) and learning a lot, including new technologies and more about **blockchains/cryptocurrency** was a challenge, but we are glad that we did it. We managed to create a fundraising platform that eliminates most of the flaws that common fundraising platforms have and empowers users/fundraisers all around the world with support for a multitude of assets, including both cryptocurrencies and fiat currencies. We are also proud to implement various APIs and SDKs like Stellar to create user-friendly features for our website, such as a **QR code creator** for each fundraiser and **encryption**. 

## What we learned
At first, none of us even knew what blockchains were but through this hackathon, we learned a lot about Stellar, blockchains and decentralized networks in general. The future of these technologies excites us as they allow for improved transparency and accessibility. 

On the technical side, we had to learn how to integrate Stellar into our full-stack web app while also managing our database effectively and securely. We also improved our frontend and Python skills to build our web app (all of this is a result of constant googling/learning!) .

## What's next for CryptPool
Our group plans to continue working on CryptPool and our big goal for this project is to **publicly release** CryptPool, as a direct competitor to popular fundraising websites, emphasizing our global and feeless advantages as our selling point. We see CryptPool as having a massive potential to bridge together the global community to help those in need without the **financial shackles** (limited supported currencies & fees) of common crowdfunding websites. 

Before doing this, we would need to continue improving the security, UI/UX, and features of our website, as a few dozen hours just isn’t enough for our vision. Another small addition that we would like to add would be an option for fundraisers to automatically exchange their donated assets into their desired assets, taking advantage of Stellar’s decentralized exchange. This would allow for **more flexibility** for some fundraisers as it would make the withdrawal process a lot smoother/easier for certain users. 
