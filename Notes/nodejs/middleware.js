/* In an Express.js application, middleware plays a crucial role in handling requests and responses
 
***Application-Level Middleware:
 Application-level middleware is bound to the entire application using app.use() or specific HTTP methods (e.g., app.get(), app.post()).] */
// example
app.use((req, res, next) => {
    console.log('Time:', Date.now());
    next(); // Pass control to the next middleware
});
  

/*  ***Router-Level Middleware:
 Router-level middleware is applied to specific routes using router.use() or HTTP methods within a router.
 It allows you to handle middleware for specific paths.  */
const userRouter = express.Router();
userRouter.use('/user/:id', (req, res, next) => {
  console.log('Request Type:', req.method);
  next();
});

/*   ***Error-Handling Middleware:
 Error-handling middleware is used to handle errors during request processing.
 It typically appears at the end of the middleware stack. */
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something went wrong!');
  });
  
//    ***Built-In Middleware
// Express provides built-in middleware functions like express.json() (for parsing JSON), 
/* It allows the server to parse incoming requests with JSON payloads. When a client sends data to the server in the form of JSON (e.g., via an HTTP POST request, from a form submission or an API call ), 
 this middleware parses the JSON data and makes it available in the request.body object. */

 app.use(express.json());
//  This line should be placed before your route handlers so that it can process incoming requests before they reach your route logic.

//  express.urlencoded() (for parsing URL-encoded data), and express.static() (for serving static files).
/* When a client submits an HTML form with method="POST" and enctype="application/x-www-form-urlencoded", the data is sent as URL-encoded key-value pairs.
The express.urlencoded() middleware parses this data and makes it accessible in the request.body object. */

// Third-Party Middleware:
// You can also use third-party middleware packages available on npm.
// Examples include morgan for logging, helmet for security, and cors for handling cross-origin requests