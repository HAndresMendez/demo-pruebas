# Hello World JS

A pretty simple "Hello World" application written using Node.js. Nothing fancy, just functional.

This sample has a few important files:

- an `.env` file containing all the environment variables
- a `Dockerfile`, which will build the container image based on the source code
- Node dependencies on the `package-lock` and `package` JSON files.
- `server.js` the fancy little program

## Run app locally

CD to the repository directory:

```bash
cd /repository/directory
```

- - - 

Build the image:

```bash
docker build . --tag <image_tag>
```

**Note:** for using IBM Container registry, `<image_tag>` format should be `us.icr.io/<my_namespace>/<my_repository>:<my_tag>`

- - - 

Run it:

```bash
docker run -p 8080:8080 <image_tag>
```

**Note:** another port could be used. Validate if project has an environment variable defined or it.

- - - 

If you can't remember the image tag, list them by running:

```bash
docker image list
```