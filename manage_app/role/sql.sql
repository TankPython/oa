INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (1, 0, NULL, '权限管理', '/', 0, 0, '/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (2, 0, NULL, '个人事务管理', '/', 0, 0, '/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (3, 0, NULL, '公告管理 ', '/', 0, 0, '/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (4, 0, NULL, '人事管理 ', '/', 0, 0, '/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (5, 0, NULL, '用户管理 ', '/', 1, 1, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (6, 0, NULL, '角色管理 ', '/', 1, 1, '/api/role/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (7, 0, NULL, '事务申请 ', '/', 4, 1, '/api/personal_manage/up');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (8, 0, NULL, '个人信息', '/', 2, 1, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (9, 0, NULL, '事务申请', '/', 2, 1, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (10, 0, NULL, '意见反馈', '/', 2, 1, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (11, 0, NULL, '获取用户', 'get', 5, 2, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (12, 0, NULL, '编辑用户', 'put', 5, 2, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (13, 0, NULL, '删除用户', 'delete', 5, 2, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (14, 0, NULL, '添加用户', 'post', 5, 2, '/api/user/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (15, 0, NULL, '获取角色', 'get', 6, 2, '/api/role/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (16, 0, NULL, '编辑角色', 'put', 6, 2, '/api/role/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (17, 0, NULL, '删除角色', 'delete', 6, 2, '/api/role/');
INSERT INTO `os_system`.`oa_permission`(`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES (18, 0, NULL, '添加角色', 'post', 6, 2, '/api/role/');


INSERT INTO `os_system`.`oa_role`(`id`, `deleted`, `deleted_at`, `name`, `desc`, `ps_ids`) VALUES (1, 0, NULL, '主管77', '人事主管', '1,5,11,12,6,15,16,2,8,9,10,3,4,7');
INSERT INTO `os_system`.`oa_role`(`id`, `deleted`, `deleted_at`, `name`, `desc`, `ps_ids`) VALUES (2, 0, NULL, '总监', '研发总监', '');
INSERT INTO `os_system`.`oa_role`(`id`, `deleted`, `deleted_at`, `name`, `desc`, `ps_ids`) VALUES (20, 0, NULL, '343', '4343', '');
INSERT INTO `os_system`.`oa_role`(`id`, `deleted`, `deleted_at`, `name`, `desc`, `ps_ids`) VALUES (21, 0, NULL, 'err', 'erer', '');
INSERT INTO `os_system`.`oa_role`(`id`, `deleted`, `deleted_at`, `name`, `desc`, `ps_ids`) VALUES (22, 0, NULL, 'admin', '超级管理员', '1,5,11,12,13,6,15,16,17,2,8,9,10,3,4,7');
INSERT INTO `os_system`.`oa_role`(`id`, `deleted`, `deleted_at`, `name`, `desc`, `ps_ids`) VALUES (23, 0, NULL, '3', '3', NULL);


INSERT INTO `os_system`.`oa_user`(`id`, `deleted`, `deleted_at`, `name`, `email`, `phone`, `role_id`, `password`) VALUES (15, 0, NULL, 'test2', 'efffef', '234343', 22, 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `os_system`.`oa_user`(`id`, `deleted`, `deleted_at`, `name`, `email`, `phone`, `role_id`, `password`) VALUES (21, 0, NULL, 'tank', '', '', 1, 'e10adc3949ba59abbe56e057f20f883e');
