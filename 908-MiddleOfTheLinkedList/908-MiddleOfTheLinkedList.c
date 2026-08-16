// Last updated: 16/08/2026, 12:33:34
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int count = 0;
    struct ListNode* ptr = head;
    struct ListNode* temp = head;
    while (ptr != NULL){
        ptr = ptr -> next;
        count ++;
    }
    for(int i=0; i<(count/2);i++){
        temp =temp ->next;
    }
    return temp ;
}