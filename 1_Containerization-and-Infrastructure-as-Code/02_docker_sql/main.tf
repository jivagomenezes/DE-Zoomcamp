# Terraform Block: Specifies the required providers for the project
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}
# Google Provider Configuration
provider "google" {
  credentials = file("/home/jivagomenezes/.config/gcloud/application_default_credentials.json")
  project = "zoomcamp-airflow-456109"
  region  = "europe-west1"
}
# Google Cloud Storage Bucket
resource "google_storage_bucket" "data-lake-bucket" {
  name          = "zoomcamp-data-lake-jivago-2025"
  location      = "EU"
  # Optional, but recommended settings:
  storage_class = "STANDARD"
  uniform_bucket_level_access = true
  versioning {
    enabled     = true
  }
  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30  // days
    }
  }
  force_destroy = true
}
# Google BigQuery Dataset
resource "google_bigquery_dataset" "dataset" {
  dataset_id = "ny_taxi_data"
  project    = "zoomcamp-airflow-456109"
  location   = "EU"
}