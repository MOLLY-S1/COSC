def find_culprit(server_log):
    # Iterate through the log and check for the first 500 response code
    for i in range(1, len(server_log)):
        if server_log[i][1] == 500:
            # If the current request has a 500 error, return the IP of the previous request
            return server_log[i - 1][0]

    # If no 500 code is found, or if no request precedes a 500, return None
    return None


# Example usage:
server_log_example = [
    ('192.168.0.1', 200),
    ('192.168.0.2', 200),
    ('192.168.0.3', 500),
    ('192.168.0.4', 404),
    ('192.168.0.5', 500)
]

culprit_ip = find_culprit(server_log_example)
print(culprit_ip)  # Expected output: '192.168.0.2'
