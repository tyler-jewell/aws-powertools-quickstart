"""Lambda Powertools Python Tutorial."""

from aws_lambda_powertools.logging import Logger, correlation_paths

logger = Logger(service="APP")


def hello_name(name):
    """Return a friendly greeting."""
    logger.info("Request from %s received", name)
    return {"message": f"hello {name}!"}


def hello():
    """Return a friendly greeting."""
    logger.info("Request from unknown received")

    return {"message": "hello unknown!"}


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.API_GATEWAY_REST, log_event=True
)  # type: ignore
def lambda_handler(event, context):
    """Lambda handler."""
    return hello_name(event["name"]) if "name" in event else hello()
