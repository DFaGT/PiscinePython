from typing import Iterable, Generator, TypeVar

T = TypeVar('T')

def ft_tqdm(iterable: Iterable[T]) -> Generator[T, None, None]:
    """
    A simple tqdm-like progress bar generator.

    Args:
        iterable: An iterable of items to process.

    Yields:
        Each item from the iterable, while displaying a progress bar.
    """
    total = len(iterable)
    if total == 0:
        return

    bar_length = 50
    for i, item in enumerate(iterable, start=1):
        # Calculate progress
        filled = int(bar_length * i / total)
        if filled <= 0:
            bar = '>' + ' ' * (bar_length - 1)
        elif filled >= bar_length:
            bar = '=' * bar_length
        else:
            bar = '=' * (filled - 1) + '>' + ' ' * (bar_length - filled)

        percent = i / total * 100
        # Print the progress bar
        print(f"\r{percent:3.0f}%|[{bar}] {i}/{total}", end='', flush=True)

        yield item

    # Finish with a newline
    print()
