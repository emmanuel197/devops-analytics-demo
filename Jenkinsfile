// CI pipeline for the TaskBoard app.
// Mirrors a typical GitHub Actions workflow: checkout -> build -> test.
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Building commit ${env.GIT_COMMIT ?: 'local'}"
            }
        }

        stage('Build image') {
            steps {
                // Build the same Docker image we ship. ${BUILD_NUMBER} tags each run.
                sh 'docker build -t taskboard:${BUILD_NUMBER} -t taskboard:latest app/'
            }
        }

        stage('Test') {
            steps {
                // Run the Django test suite inside the freshly built image.
                // --entrypoint sh skips the prod entrypoint (which needs Postgres);
                // DJANGO_TEST_SQLITE=1 makes tests use in-memory SQLite.
                sh '''docker run --rm \
                        -e DJANGO_TEST_SQLITE=1 \
                        --entrypoint sh \
                        taskboard:${BUILD_NUMBER} \
                        -c "python manage.py test --verbosity=2"'''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline succeeded: image built and all tests passed.'
        }
        failure {
            echo '❌ Pipeline failed: check the stage logs above.'
        }
    }
}
