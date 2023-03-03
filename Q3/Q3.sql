-- rank the category diversity of each owner

SELECT
  article_category.owner_id,
  article_category.owner_name,
  COUNT(DISTINCT category) AS category_diversity
FROM
    (
        
        SELECT 
            article.owner_id AS `owner_id`,
            owner.owner_name AS `owner_name`,
            category_article_mapping.category_id AS category
        FROM 
            article
        INNER JOIN
            owner on article.owner_id = owner.owner_id
        INNER JOIN 
            category_article_mapping
        ON article.article_id = category_article_mapping.article_id
    ) as `article_category`
GROUP BY (`article_category`.`owner_id` , `article_category`.`owner_name`)