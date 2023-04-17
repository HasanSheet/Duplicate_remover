import argparse

def remove_duplicates(input_file, output_file):
    unique_urls = set()
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line not in unique_urls:
                unique_urls.add(line)
    
    with open(output_file, 'w') as file:
        for url in unique_urls:
            file.write(url + '\n')
    
    print(f"Duplicate URLs removed. Unique URLs written to {output_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove duplicate URLs from a text file.')
    parser.add_argument('input_file', metavar='input_file', type=str, help='Input text file containing URLs')
    parser.add_argument('-o', '--output_file', type=str, help='Output text file to write unique URLs (default: unique_urls.txt)', default='unique_urls.txt')
    args = parser.parse_args()
    
    remove_duplicates(args.input_file, args.output_file)

