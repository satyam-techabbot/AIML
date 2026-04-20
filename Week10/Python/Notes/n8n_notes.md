# N8N

n8n is a powerful, extendable workflow automation tool that allows you to connect different apps and services to automate tasks.

Unlike many other automation platforms, it uses a node-based visual approach, giving you a high degree of control over how data moves between systems.

---

## Core Internal Components
The n8n architecture consists of several specialized layers: 

- Visual Editor (Frontend): 

    A visual builder where users design workflows. It converts the visual graph into a JSON object and sends it to the backend for storage and execution.

- Execution Engine (Backend): 

    The core service that reads workflow definitions, creates an Execution Context (unique ID, input data, and metadata), and runs nodes step-by-step.

- Node System:

    Modular units written in JavaScript/TypeScript. They are categorized as Trigger Nodes (start the flow), Action Nodes (perform tasks), and Logic Nodes (handle branching/looping).

- Task Runners:

    For complex operations like custom JavaScript or Python, n8n uses Task Runners. These can run as child processes or in separate "sidecar" containers to isolate heavy compute tasks from the main engine.

- Database: 

    Stores workflow metadata, user credentials, and historical execution logs. It defaults to SQLite but typically uses PostgreSQL in production.

---

## Self-hosting vs. Cloud
One of the biggest reasons people choose n8n over competitors like Zapier is the ability to self-host.

This means instead of the software running on n8n's servers, it runs on your own hardware (like a home server, a Raspberry Pi, or a private virtual server).

| Feature | n8n Cloud| Self-Hosted (Desktop/Server) | 
| ------- | -------- | ---------------------------- |
| Setup   | Instant; no technical work. | Requires Docker or Node.js knowledge. |
| Data Privacy | Managed by n8n. | Total control; data never leaves your server. |
| Cost | Monthly subscription. | Free (Fair-code license for personal use). |
| Access | Web-based from anywhere. | Requires manual setup for external access. |

---

## Nodes and Workflows
Every automation in n8n is built using Nodes. Think of a node as a single step in a factory assembly line.

There are two main types of nodes that start and run the process:
- Trigger Nodes: These are the "starters." They wait for something to happen, like a new email arriving, a specific time of day, or a person filling out a form. 🏁

- Action Nodes: These are the "doers." Once the trigger goes off, these nodes perform a task, like sending a Slack message, creating a row in a Google Sheet, or resizing an image. 🛠️

To connect them, you literally draw a line from the output of one node to the input of the next. Data flows through these lines like water through a pipe.

---

## Advanced Logic and Data
While simple "Trigger ➔ Action" flows are great, n8n shines when things get complicated. This is where we move from a straight line to a branching tree.

There are two main ways to handle complex logic in n8n:
- The If Node (Branching): This allows your workflow to make decisions. For example, if the X post is positive, send it to Slack; if it's negative, create a ticket in a support tool like Zendesk.

- The Code Node (JavaScript): Sometimes a pre-built node doesn't exist for exactly what you need. n8n allows you to write small snippets of JavaScript (or Python) to transform your data. For instance, you could write a script to calculate a discount or reformat a messy date string.

#### Example: Filtering Data
Imagine your X trigger brings in a lot of "noise"—posts that mention your company but are just spam. You only want to save posts that have more than 10 likes.

In this case, you would place an If Node between the X trigger and the Google Sheet action.

```javascript
const spamWords = ['ad', 'sponsored', 'promo', 'deal'];
const text = $node["X Trigger"].json["text"].toLowerCase();

// Check if any spam word is in the text
const isSpam = spamWords.some(word => text.includes(word));

return { isSpam };
```

---

## Practical Example:
On customer making an order, if total purchase is equal to or greater than 100 then send them an email of  10% discount, discount coupon. 

- Step 1:
    Creating First Node: 
    - Add Node
    - Select "Webhook"
    - Set HTTP Methond as 'POST'
    - Set path to ur liking 'new-order-test'
    - And other setting if required or leave it as it is.

- Step 2:
    Writing logic code in python to send json data with logic.
    - access previous node's output as input using _item or _items
    ```python
    data = _item["json"]["body"]
    email = data.get("email")
    name = data.get("customer_name", "Valued Customer").title()
    price = float(data.get("total_price", 0))

    return {
        "email": email,
        "name": name,
        "price": price,
        "discount_code": "WELCOME10" if price >= 100 else ""
    }
    ```

- Step 3:
    Add if node for branching of logic/node:
    - Put expression in 'value 1'
    - select the comparison operator and datatype
    - Add value 2

- Step 4:
    True Branch. To send an email, create an email node and 'send a message'
    - Input 'SMTP Credential' and enter details
    - Fill all info including from and to email n etc.
    - Prepare HTML message to return discount coupon and greetings to the user

- Step 5:
    False Branch. To send an email, create an email node and 'send a message'
    - Input 'SMTP Credential' and enter details
    - Fill all info including from and to email n etc.
    - Prepare HTML message to return greetings to the user.
    
- Step 6:
    POST: https://satyam-techabbot.app.n8n.cloud/webhook-test/new-order-test

    JSON Content:
    ```json
    {
        "email": "ysat2104@gmail.com",
        "customer_name": "john doe",
        "total_price": 101
    }
    ```

---






