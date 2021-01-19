# Day 20 CFG

## Notation

**bold**: terminal

{}: can repeat any number of times (including 0)

|: or

## Grammar

regex -> **^** chunk-list **$**

chunk-list -> chunk { **|** chunk }

chunk -> { dir-str | paren }

paren -> **(** chunk-list **)**

dir-str -> { direction }

direction -> **N** | **S** | **W** | **E**
