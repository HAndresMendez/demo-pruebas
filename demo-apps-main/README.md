# DEMO APPS

This repository is meant to store small demo applications for showcasing IBM Cloud services like Code Engine, Red Hat OpenShift, Kubernetes Service, among others. I've decided to leave this repo public in case someone else wants to try them out.

- [DEMO APPS](#demo-apps)
  - [Catalog](#catalog)
  - [Run containerized apps locally](#run-containerized-apps-locally)
  - [Push images to ICR](#push-images-to-icr)

## Catalog

The available demos apps are:

- [connect-mongodb-py](./connect-mongodb-py)
  - **Description:** application that inserts a JSON on a MongoDB database containing the current day and time.
  - **Use Cases:** FaaS-related use cases, be it on Cloud Functions or Code Engine. Examples of application integration, or batch processes (Code Engine Jobs).
- [hello-world-js](./hello-world-js/)
  - **Description:** exposes a server (on port 8080 by default) with a "Hello ${TARGET}" message.
  - **Use Cases:** application deployment on any PaaS service (RHOS, IKS, CE). **Update:** can also be used to show how environment variables work, since I've added them for both `TARGET` and `PORT`.
- [send-email-app](./send-email-app)
  - **Description:** application that sends emails via SendGrid. **Note:** it is untested due to invalid SendGrid credentials.
  - **Use Cases:** FaaS-related use cases, be it on Cloud Functions or Code Engine. Examples of on-demand code executions.

## Run containerized apps locally

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

## Push images to ICR

Push image to IBM Container Registry (ICR) by running:

```bash
docker push <image_tag>
```

Where `<image_tag>` has the following format: `<region>.icr.io/<namespace>/<repository>:<tag>`. For more info about regions, [check out the docs](https://cloud.ibm.com/docs/Registry?topic=Registry-registry_overview#registry_regions).

- - - 

If the image isn't tagged this way, fix it by re-tagging it. Just run:

```bash
docker tag <current_tag> us.icr.io/<namespace>/<repository>:<tag>
```