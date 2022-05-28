from file_reader import FileReader
from subscriber import MaxLenLineSubscriber, MaxLenWordSubscriber, WordCounterSubscriber, LineWithLongestWordSubscriber


def main():
    max_len_line_sub = MaxLenLineSubscriber()
    max_len_word_sub = MaxLenWordSubscriber()
    word_counter_sub = WordCounterSubscriber()
    line_with_longest_word_sub = LineWithLongestWordSubscriber()

    file_reader = FileReader('resources/input01.txt')
    file_reader.subscribe(max_len_line_sub)
    file_reader.subscribe(max_len_word_sub)
    file_reader.subscribe(word_counter_sub)
    file_reader.subscribe(line_with_longest_word_sub)

    file_reader.read_by_line()

    print('-' * 80)
    print(f"Max len line: {max_len_line_sub.get_max_len_line()}")
    print(f"Max len word: {max_len_word_sub.get_max_len_word()}")
    print(f"Word count: {word_counter_sub.get_word_count()}")
    print(f"Line with longest word: {line_with_longest_word_sub.get_line_with_longest_word()}")


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Read: Seoul -15 42 766
    # Read: Seoul 27 85 790
    # Read: Kyiv -36 46 768
    # Read: Kyiv -10 80 771
    # Read: London -40 77 727
    # Read: London -18 85 710
    # Read: Seoul 15 65 795
    # Read: London 33 87 745
    # Read: Washington 39 66 776
    # Read: Washington 16 60 769
    # Read: London -32 27 768
    # Read: London -18 84 796
    # Read: Kyiv -31 57 715
    # Read: Seoul 34 75 781
    # Read: Kyiv -7 32 721
    # Read: London 34 31 783
    # Read: Seoul 14 51 763
    # Read: Kyiv 4 27 736
    # Read: London 26 18 793
    # Read: Washington 9 83 778
    # Read: Washington -46 52 784
    # Read: Seoul -23 76 772
    # Read: Seoul -41 7 773
    # Read: London 33 84 744
    # Read: Washington -9 3 763
    # Read: Kyiv 4 91 716
    # Read: Seoul -37 64 712
    # Read: London 48 41 775
    # Read: Washington 0 34 790
    # Read: Kyiv -10 21 776
    # Read: Kyiv 42 74 799
    # Read: London -14 50 742
    # Read: Kyiv 39 74 792
    # Read: Kyiv 49 49 747
    # Read: Kyiv -35 12 742
    # Read: London 16 33 722
    # Read: London 9 97 711
    # Read: London -50 68 734
    # Read: Seoul -31 94 700
    # Read: Kyiv 27 27 796
    # Read: London -29 10 761
    # Read: Kyiv -19 56 701
    # Read: London -22 1 713
    # Read: London -49 41 778
    # Read: Washington 28 69 797
    # Read: Seoul -14 29 710
    # Read: Seoul 42 38 759
    # Read: Washington 19 4 757
    # Read: Seoul -10 17 754
    # Read: Kyiv 18 95 736
    # Read: Seoul -7 73 786
    # Read: Washington -19 11 724
    # Read: London -31 44 735
    # Read: Washington -23 21 781
    # Read: Washington -27 44 706
    # Read: Seoul 33 79 743
    # Read: London -30 26 742
    # Read: London -2 34 748
    # Read: Seoul -39 74 703
    # Read: Kyiv -47 74 772
    # Read: London 3 18 792
    # Read: London -25 86 754
    # Read: London 47 40 712
    # Read: Washington -14 86 796
    # Read: London -3 75 797
    # Read: London -6 93 783
    # Read: Seoul -26 24 735
    # Read: Washington -31 23 800
    # Read: London 43 51 751
    # Read: Washington 32 40 787
    # Read: Kyiv -11 91 797
    # Read: London -19 53 752
    # Read: Washington -33 36 744
    # Read: London 49 28 722
    # Read: London 24 53 772
    # Read: Seoul -29 15 713
    # Read: London 50 7 768
    # Read: London 18 94 733
    # Read: Washington -8 89 745
    # Read: Kyiv -8 69 797
    # Read: Seoul 1 97 765
    # Read: London -28 49 793
    # Read: Washington 23 24 756
    # Read: Kyiv 10 24 701
    # Read: London -5 33 718
    # Read: Seoul -14 56 765
    # Read: London -46 17 727
    # Read: Washington 14 64 769
    # Read: London -16 7 748
    # Read: Kyiv 32 22 703
    # Read: Kyiv -1 59 757
    # Read: Kyiv -44 14 731
    # Read: Kyiv -44 82 778
    # Read: London 32 19 703
    # Read: London -48 25 795
    # Read: Washington -28 51 776
    # Read: London -3 90 783
    # Read: Kyiv -20 80 778
    # Read: Washington 46 60 723
    # Read: London 36 10 744
    # Read:
    # --------------------------------------------------------------------------------
    # Max len line: Washington -46 52 784
    # Max len word: Washington
    # Word count: 100
    # Line with longest word: Washington 39 66 776
