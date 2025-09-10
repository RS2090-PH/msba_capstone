# Problem Statement: Reducing Cart Abandonment on MyCoke360


# Business Problem:


-	Swire Coca Cola recently launched MyCoke360, a new B2B digital ordering platform for its Food Service On Premise (FSOP) customers. 
-	A key challenge arising with this new platform is cart abandonment, where customers add items to their online cart but do not complete the purchase by their next scheduled order date.
    -	This behavior is costly as it leads to losses in potential revenue. It obscures the understanding of customer interaction on the new platform. This creates a significant opportunity cost, as potential sales are lost due to unresolved issues in the customer's digital purchasing journey.


# Benefits of a solution:

-	A detailed analysis of this problem through Exploratory Data Analysis and developing Machine Learning models will provide critical insights into exploring customer behavior. 
-	The primary benefits include:
    -	Identifying specific behavioral patterns, user actions, or sequences of events that are strong predictors of both cart abandonment and even cart recovery.
    -	Delivering actionable, data driven recommendations to Swire Coca-Cola to optimize the MyCoke360 platform, improve order completion rates, and enhance the overall user experience to retain and acquire new clientele.
    -	Reducing revenue loss by understanding and addressing the main causes of why customers fail to complete their orders and leave them abandoned.


# Analytics Approach:


-	The project will analyze customer interaction data from the MyCoke360 platform to uncover the drivers of cart abandonment. <br>
-	The analysis will be centered on: <br>
    - Google Analytics (GA) event data, supplemented by internal Orders, Sales, Customer, and Material dimension tables to build a complete picture of user behavior.
        - An Order Window which is the time between two expected order dates for a customer will be established to define whether a cart is officially abandoned. Initially we will analyze the anchor day and purchases to identify abandoned orders.
        - The primary goal is to use this combined dataset to identify the behavioral patterns, product characteristics, and device specific issues that most significantly influence cart abandonment and recovery, ultimately providing Swire Coca-Cola with targeted recommendations and illustrating them by implementing storytelling with data principles.
- The model itself is still undecided. Potential models could assign abandonment as a Boolean:
    - 0: Indicating if an order was abandoned.	
    - 1: Indicating if a purchase was ordered before or on its anchor day.
- Options for a binary model include:
    - Logistic Regression.
    - XGBoost.
    - Random Forest.
    - Other effective models identified throughout the analysis.


# Success Metrics:

-	The success of this project will be measured by the clarity and utility of the insights provided. A few of the Key metrics include:
    - Quantified Financial Impact: A clear measure of the total dollar value of products in abandoned carts, compared against total platform revenue. Per previous conversations with the Swire stakeholders, NSI_DEAD_NET is the appropriate column that captures Gross Profit and Revenue to analyze sales.
    -	Predictive Behavioral Insights: The successful identification of user events, device types, and customer groups that have the highest correlation with cart abandonment and cart recovery. While correlation is not equivalent to causation, insights of correlation are useful to observe trends.
    -	Actionable Product Analysis: A comprehensive report detailing which specific products, brands, pack types, or flavors appear most frequently in abandoned carts. A minor challenge with this arises when customers place mobile orders. Items purchase for such orders are left blank therefore requiring merging other tables to capture that information.
    -	Post Abandonment Customer Journey Mapping: A clear understanding of whether a customer who abandons a cart proceeds to order through a different method or becomes inactive. A clear definition of cart abandonment must be established. It is possible that a customer ordered their cart items for the following cycle. Orders must be analyzed on a granular basis to determine if they are abandoned or simply postponed.


# Scope:

- Within Scope:
    - Analyzing Google Analytics and internal sales/order data to identify behavioral patterns.
    - Defining and measuring the financial impact of cart abandonment on MyCoke360 revenue in a concrete format.
    - Developing and presenting a final report with key findings and strategic recommendations through data storytelling to improve order completion rates.
- Out of Scope:
    - The technical implementation of any changes to the MyCoke360 website or application.
    - The creation of marketing campaigns to re capture users with abandoned carts.
    - Adjusting the specifics namely the product pricing, inventory, or overall sales strategy based on the findings.


# Details:

- Completed by:
    - Ali Ladha, Robert Stohel, Cyrus Sobhani, Sterling Leduc.
- Timeline:
    - November 1, 2025: Rough draft for the presentation.
    - November 16, 2025: Project to be finalized with a presentation.
- Milestones:
    - August 31, 2025: Group selection and project kickoff.
    - September 6, 2025: Initial meeting to delegate tasks and responsibilities.
    - September 13, 2025: Establishing the true business problem and aligning it with all team members.
    - October 4, 2025: Exploratory data analysis with Data cleaning completed.
    - October 18, 2025: Prototype Model completed.
    - October 25, 2025: Selecting the most accurate models created by the group.
    - November 1, 2025: Submitting the practice presentation recording.
    - November 8, 2025: Final revisions to the presentation.
    - November 15, 2025: Submitting the final presentation slides.
    - November 16, 2025: Final presentation delivery to stakeholders.





