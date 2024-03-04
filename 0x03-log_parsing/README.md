# Script Metrics Calculator

This script reads standard input (stdin) line by line and computes various metrics based on the input format. The input format must follow the following pattern:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

If the input line does not match this format, it will be skipped. The script will print the statistics every 10 lines or upon receiving a keyboard interruption (CTRL + C).

## Usage

To run the script, execute the following command:

```bash
python metrics_calculator.py
```

Make sure you have Python installed on your system.

## Output

The script will compute the following metrics and display them after every 10 lines or upon keyboard interruption:

- **Total file size:** The sum of all previous file sizes encountered in the input.
- **Number of lines by status code:** The count of lines for each of the following status codes: 200, 301, 400, 401, 403, 404, 405, and 500. Only integer status codes that appear in the input will be considered.

The statistics will be printed in ascending order of the status codes.

## Example

Suppose we have the following input:

```
192.168.0.1 - [2023-07-01] "GET /projects/260 HTTP/1.1" 200 256
192.168.0.2 - [2023-07-02] "GET /projects/260 HTTP/1.1" 404 404
192.168.0.3 - [2023-07-03] "GET /projects/260 HTTP/1.1" 200 512
192.168.0.4 - [2023-07-04] "GET /projects/260 HTTP/1.1" 301 256
192.168.0.5 - [2023-07-05] "GET /projects/260 HTTP/1.1" 500 1024
192.168.0.6 - [2023-07-06] "GET /projects/260 HTTP/1.1" 200 128
```

After processing the above input, the script will display the following statistics:

```
Total file size: 2576
200: 3
301: 1
404: 1
500: 1
```