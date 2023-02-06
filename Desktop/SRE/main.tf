// Settings for the google cloud account
// Write the path to the json key giving access to the project
provider "google" {
  project = "premium-portal-323320"
  region  = "us-central1"
  zone    = "us-central1-a"
}

// Ressource 1: cloud run service running the docker image
// Write the path to the docker image hosted in the google container registry
// To set up this resource with Terraform, the service account key used 
// must have the appropriate permissions.
resource "google_cloud_run_service" "default" {
  name     = "sre2"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "gcr.io/premium-portal-323320/sre:latest"
        ports { 
          container_port = 80
}
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

// Ressource 2: gives to non authenticated users access to the web page
// To set up this resource with Terraform, the service account key used 
// must have the appropriate permissions.
data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.default.location
  project     = google_cloud_run_service.default.project
  service     = google_cloud_run_service.default.name

  policy_data = data.google_iam_policy.noauth.policy_data
}