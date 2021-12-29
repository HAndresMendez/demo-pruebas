# Hello World

A pretty simple Node.js application. It sends an email and says "Hello!". Pretty cool, huh?

- - -

## Run locally

CD to the repository directory:

```bash
cd /repository/directory
```

Build the image:

```bash
docker build . <image_tag>
```

**Note:** for using IBM Container registry, `<image_tag>` format should be `us.icr.io/<my_namespace>/<my_repository>:<my_tag>`

Run it:

```bash
docker run -p 8080:8080 <image_tag>
```

If you can't remember the image tag, run:

```bash
docker image list
```

To list all built images.
