INSERT INTO `oa_permission` (`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES('1','0',NULL,'权限管理','get','0','0','/api/user_manage');
INSERT INTO `oa_permission` (`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES('2','0',NULL,'个人事务管理','get','0','0','/api/personal_manage');
INSERT INTO `oa_permission` (`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES('3','0',NULL,'公告管理 ','get','0','0','/api/public_manage');
INSERT INTO `oa_permission` (`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES('4','0',NULL,'人事管理 ','get','0','0','/api/hr_manage');
INSERT INTO `oa_permission` (`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES('5','0',NULL,'用户管理 ','get','1','1','/api/role_manage/user');
INSERT INTO `oa_permission` (`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES('6','0',NULL,'角色管理 ','get','1','1','/api/role_manage/role');
INSERT INTO `oa_permission` (`id`, `deleted`, `deleted_at`, `name`, `method`, `pid`, `level`, `path`) VALUES('7','0',NULL,'事务申请 ','get','4','1','/api/personal_manage/up');