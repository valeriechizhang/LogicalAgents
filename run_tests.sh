#!/bin/bash

MYNAME=`basename "$0"`

if [ "$#" -ne '1' ]
then
  echo "Usage: $MYNAME <test_directory>" 1>&2
  exit 1
fi

TEST_DIR="$1"
RESULTS_DIR="test_results"

die() {
  echo "$1" 1>&2
  exit 1
}

mkdir -p $RESULTS_DIR || die "Failed to create $RESULTS_DIR"

RESULT_PASS=0
RESULT_FAIL_TO_RUN=0
RESULT_FAIL_TO_COMPARE=0
ANON_TEST_NUM=1

echo

# Make sure that we can find the test files in the cwd
export PYTHONPATH="`pwd`:$PYTHONPATH"
echo $PYTHONPATH

for test_filename in `ls -1 $1 | grep '\.py$' | sort`
do
  str="$test_filename"
  full_filename="$TEST_DIR/$test_filename"

  # Verify that an expected output file exists
  good_out_filename=`echo $test_filename | sed -e 's/\.py$/.out/'`
  if [ "$good_out_filename" == "$test_filename" ] || ! [ -f "$TEST_DIR/$good_out_filename" ]
  then
    die "Cannot find expected output file $good_out_filename for test $test_filename"
  fi
  good_out_filename="$TEST_DIR/$good_out_filename"
  test_out_file="$RESULTS_DIR/${test_filename}.out"
  echo -n "TEST $ANON_TEST_NUM ($test_filename)..."
  ANON_TEST_NUM=$((ANON_TEST_NUM+1))
  python "$full_filename" > $test_out_file 2>&1

  if [ "$?" -ne '0' ]
  then
    echo "FAILED TO RUN"
    RESULT_FAIL_TO_RUN=$((RESULT_FAIL_TO_RUN+1))
    continue
  fi

  if ! cmp -s "$test_out_file" "$good_out_filename"
  then
    echo "FAIL"
    RESULT_FAIL_TO_COMPARE=$((RESULT_FAIL_TO_COMPARE+1))
    continue
  fi

  echo "PASS"
  RESULT_PASS=$((RESULT_PASS+1))
done

echo
echo "SUMMARY"
echo "~~~~~~~"
echo "PASSES: $RESULT_PASS"
echo "FAILURES: $RESULT_FAIL_TO_COMPARE"
echo "FAILED TO RUN: $RESULT_FAIL_TO_RUN"
echo

