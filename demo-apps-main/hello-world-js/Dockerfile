# Import Node image
FROM node:12-alpine

# Copy files into container
COPY . .

# Install dependencies
RUN npm install

# Define env variable PORT
ENV PORT=8080

# Expose PORT
EXPOSE ${PORT}

# Run program
CMD [ "node", "server.js" ]