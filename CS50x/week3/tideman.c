#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    //add index to ranks
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }

    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            //compare preferences;
            if (preferences[i][j] > preferences[j][i])
            {
                //add pair
                pairs[pair_count].winner = i;
                pairs[pair_count].loser =  j;
            }
            else if (preferences[i][j] < preferences[j][i])
            {
                //add pair
                pairs[pair_count].winner = j;
                pairs[pair_count].loser =  i;
            }
            else
            {
                continue;
            }
            // count up pair_count
            pair_count++;
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    pair temp_pair;
    // sort
    for (int i = 0; i < pair_count - 1; i++)
    {
        for (int j = i + 1; j < pair_count; j++)
        {
            //get pair point
            int i_point = preferences[pairs[i].winner][pairs[i].loser];
            int j_point = preferences[pairs[j].winner][pairs[j].loser];
            // compair point
            if (i_point < j_point)
            {
                temp_pair = pairs[i];
                pairs[i] = pairs[j];
                pairs[j] = temp_pair;
            }
        }
    }
    return;
}
// check loser already locked winner
int locked_counter(int winner, int loser)
{
    int cnt = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[i][winner] == true)
        {
            if (i == loser)
            {
                cnt++;
            }
            else
            {
                cnt += locked_counter(i, loser);
            }

        }
    }
    return cnt;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        // if locked count == 0 then locked
        if (locked_counter(pairs[i].winner, pairs[i].loser) == 0)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    
    for (int i = 0; i < candidate_count; i++)
    {
        // count lose
        int lose_count = 0;
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == true)
            {
                lose_count++;
            }
        }

        //no lose candidate is winner
        if (lose_count == 0)
        {
            printf("%s\n", candidates[i]);
            return;
        }   
    }
}
