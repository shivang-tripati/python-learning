// Besides RESTful APIs, there are other API design patterns and architectural styles that you can consider for building robust and efficient APIs. Let’s explore a few of them:
// 1. Microservice API Patterns (MAP):
/* Description: MAP, also known as Patterns for API Design, captures proven solutions to common problems encountered when specifying, implementing, and maintaining message-based APIs.
Focus: It emphasizes message representations – the payloads exchanged when APIs are called 
Categories: MAP covers various categories such as Foundation, Frontend Integration, Backend Integration, Public API, Community API, and Solution-Internal API. */

/*  Examples:
API Gateway Pattern: Acts as a central router, validating credentials and routing requests to appropriate microservices.
State Creation Pattern: Handles state creation and management within microservices.
Resource Retrieval Pattern: Fetches data from various microservices to compose a response.
Pagination Pattern: Manages large data sets by paginating results.
Quality Management Pattern: Ensures data quality and consistency across microservices.*/

/*  **2. RPC (Remote Procedure Call) APIs:
Description: RPC allows executing procedures on a remote server by passing method names and arguments.
Example Use Case: Calling a payment service to process a transaction. (gRPC in Node.js) */
// Client-side code
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('payment.proto');
const paymentService = grpc.loadPackageDefinition(packageDefinition).PaymentService;

const client = new paymentService.Payment('localhost:50051', grpc.credentials.createInsecure());

client.processTransaction({ amount: 100 }, (error, response) => {
  if (!error) {
    console.log('Transaction successful:', response);
  } else {
    console.error('Error processing transaction:', error);
  }
});


/* 3. SOAP (Simple Object Access Protocol) APIs:
Description: SOAP uses XML for structured information exchange.
Example Use Case: Integrating with legacy enterprise systems.
Code Snippet (SOAP Request):
 */

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:web="http://www.example.com/webservice">
    <soapenv:Header/>
    <soapenv:Body>
        <web:GetStockPrice>
            <web:StockName>IBM</web:StockName>
        </web:GetStockPrice>
    </soapenv:Body>
</soapenv:Envelope>

/* GraphQL APIs:
Description: GraphQL allows clients to specify the data they need from an API.
Example Use Case: Building a real-time chat application.
 */
// query {
//     user(id: "123") {
//       name
//       email
//     }
//   }
  

/*WebSocket APIs:
Description: WebSockets enable bidirectional communication between clients and servers.
Example Use Case: Real-time chat applications.
Code Snippet (WebSocket Client in JavaScript)  */

const socket = new WebSocket('wss://example.com/chat');

socket.addEventListener('open', (event) => {
  socket.send('Hello, server!');
});

socket.addEventListener('message', (event) => {
  console.log('Received:', event.data);
});

/*  */
/*  */
/*  */
/*  */
/*  */
/*  */
/*  */
/*  */